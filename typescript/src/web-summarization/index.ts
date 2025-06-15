import axios from "axios";
import { openaiClient } from "../common/openai";
import * as cheerio from "cheerio";

const headers = {
  "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
};

class Website {
  url: string;
  title: string;
  text: string;

  constructor(url: string) {
    this.url = url;
    this.title = "";
    this.text = "";
  }

  async fetchAndParse() {
    const response = await axios.get(this.url, { headers });
    const $ = cheerio.load(response.data);

    this.title = $("title").text() || "No title found";
    $("script, style, img, input").remove();

    this.text = $("body").text().replace(/\s+/g, " ").trim();
  }
}

function userPromptForWebsite(website: Website): string {
  return `You are looking at a website titled ${website.title}. 
    The contents of this website is as follows; please provide a short summary of this website in markdown.
    If it includes news or announcements, then summarize that too. 
    Here is the content ${website.text}`;
}

const systemPrompt = `You are an assistant that analyzes the contents of a website and provides a short summary, ignoring text that might be navigation related. Respond in markdown.`;

async function summarizeWebsite() {
  const site = new Website("https://innoskrit.in");
  await site.fetchAndParse();

  const response = await openaiClient.chat.completions.create({
    model: "meta-llama/Llama-Vision-Free",
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: userPromptForWebsite(site) },
    ],
    response_format: { type: "text" },
  });

  console.log(response.choices[0].message.content);
}

summarizeWebsite();
