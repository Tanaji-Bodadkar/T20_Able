const fetch = require('node-fetch');

exports.handler = async (event) => {
  // Only allow POST requests
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    const { message, systemPrompt } = JSON.parse(event.body);
    
    // Validate message
    if (!message) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Message is required' })
      };
    }

    const response = await fetch('https://api.scitely.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.SCITELY_API_KEY}`
      },
      body: JSON.stringify({
        model: "qwen3-32b",
        messages: [
          { role: "system", content: systemPrompt || "You are FinSight AI, a professional financial advisor." },
          { role: "user", content: message }
        ],
        temperature: 0.7,
        max_tokens: 1000
      })
    });

    if (!response.ok) {
      throw new Error(`API responded with status: ${response.status}`);
    }

    const data = await response.json();
    
    return {
      statusCode: 200,
      body: JSON.stringify({ 
        reply: data.choices[0].message.content 
      })
    };
  } catch (error) {
    console.error('Error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ 
        error: 'Internal server error',
        reply: "I'm having trouble connecting to the AI service. Please try again later."
      })
    };
  }
};