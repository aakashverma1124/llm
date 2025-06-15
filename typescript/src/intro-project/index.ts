import { openaiClient } from "../common/openai";

async function sayHello() {
  const message = "Hello, this is my first message to you.";
  const response = await openaiClient.chat.completions.create({
    model: "meta-llama/Llama-3-8b-chat-hf",
    messages: [{ role: "user", content: message }],
  });

  console.log(response.choices[0].message.content);
}

sayHello();
