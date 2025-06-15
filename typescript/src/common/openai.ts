import { config } from "dotenv";
import OpenAI from "openai";

config();

const apiKey = process.env.TOGETHER_API_KEY;
if (!apiKey) throw new Error("TOGETHER_API_KEY not set");

export const openaiClient = new OpenAI({
  apiKey,
  baseURL: "https://api.together.xyz/v1", // not needed if using official openai api_key
});
