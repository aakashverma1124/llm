import { openaiClient } from "../common/openai";

async function sayHello() {
  const message = "Hello, this is my first message to you.";
  const response = await openaiClient.chat.completions.create({
    model: "meta-llama/Llama-Vision-Free",
    messages: [{ role: "user", content: message }],
  });

  console.log(response.choices[0].message.content);
}

sayHello();
