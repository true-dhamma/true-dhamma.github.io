---
title: 搜索
excerpt: Search for a page or post you're looking for
---

{% include site-search.html %}

<!-- Chatbot UI Container -->
<div id="chat-ui-wrapper">

  <!-- Collapsed Input Box (Default State) -->
  <div id="chat-collapsed-input">
    <input type="text" id="chat-input-collapsed" placeholder="向我提问..." title="向我提问..." />
    <button id="chat-send-collapsed" aria-label="发送问题">发送</button>
  </div>

  <!-- Expanded Chat Box (Hidden by default) -->
  <div id="chat-expanded-box" class="hidden">
    <div id="chat-header">
      <span>佛法问答</span>
      <button id="chat-close-button" aria-label="关闭聊天">X</button>
    </div>
    <div id="chat-messages">
      <div class="bot-message initial-message">阿弥陀佛，请问有什么可以帮助您？</div>
      <!-- Messages will be appended here -->
    </div>
    <div id="chat-input-container">
      <input type="text" id="chat-input-expanded" placeholder="输入您的问题..." title="输入您的问题..." />
      <button id="chat-send-expanded" aria-label="发送问题">发送</button>
    </div>
  </div>

</div>

<style>
  /* Base styles for the chat UI wrapper */
  #chat-ui-wrapper {
    position: fixed;
    bottom: 0; /* Align to the bottom of the viewport initially */
    right: 20px;
    z-index: 1000; /* Ensure it stays on top of other content */
    font-family: "Palatino", "Apple Garamond", Georgia, "Songti SC", "SimSun", "FangSong", serif;
    font-size: 1rem; /* Adjust base font size for readability */
    line-height: 1.5;
    color: #34495e; /* Default text color from your site */
  }

  /* Shared input/button styles, matching your site's search input */
  #chat-ui-wrapper input[type="text"],
  #chat-ui-wrapper button {
    padding: .6rem 1.2rem;
    margin-bottom: 0; /* Remove default margin from existing site CSS */
    transition: color .1s, background-color .1s, border .1s, box-shadow .1s;
    line-height: inherit;
    border: none;
    box-shadow: none;
    border-radius: 0;
    -webkit-appearance: none; /* Reset browser default styles */
    font-family: inherit;
    font-size: inherit;
  }

  #chat-ui-wrapper input[type="text"] {
    border: 1px solid #a8adac; /* From your site's input border color */
    background: #fff;
    color: #34495e;
  }
  #chat-ui-wrapper input[type="text"]:hover {
    border-color: #34495e; /* From your site's input hover border color */
  }
  #chat-ui-wrapper input[type="text"]::placeholder {
    color: #a8adac; /* Lighter placeholder for better contrast */
    opacity: 0.7;
  }
  #chat-ui-wrapper input[type="text"]:focus {
    outline: solid .12rem #fa407a; /* Focus outline from your site */
    outline-offset:-0.12rem;
  }

  #chat-ui-wrapper button {
    cursor: pointer;
    background: #3a77d8; /* Adapted from your site's link blue for buttons */
    color: white;
    box-shadow: inset 0 0 0 2rem rgba(0,0,0,0); /* Hover effect from your site's buttons */
  }
  #chat-ui-wrapper button:hover {
    box-shadow: inset 0 0 0 2rem rgba(0,0,0,.25); /* Hover effect */
  }
  #chat-ui-wrapper button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    box-shadow: none;
  }
  #chat-ui-wrapper button:focus {
    outline: solid .12rem #fa407a; /* Focus outline from your site */
    outline-offset:-0.12rem;
  }


  /* Collapsed Input Specific Styles */
  #chat-collapsed-input {
    display: flex; /* Arrange input and button horizontally */
    align-items: center;
    width: 280px; /* Default width for collapsed input on PC */
    background: white;
    border: 1px solid #ccc; /* Border from previous chat box */
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15); /* Soft shadow */
    padding: 8px 10px;
    box-sizing: border-box; /* Include padding in width calculation */
    transform: translateY(-50px); /* Lift 50px from the actual bottom:0 position */
    transition: transform 0.3s ease-out, opacity 0.3s ease-out, width 0.3s ease-out; /* Smooth transition for expansion */
  }
  #chat-collapsed-input input {
    flex-grow: 1; /* Input takes available space */
    border: none; /* Remove border from the inner input */
    padding: 0; /* Adjust padding for compact layout */
    height: 30px; /* Fixed height for consistency */
    line-height: 30px;
    box-shadow: none;
  }
  #chat-collapsed-input button {
    padding: 6px 12px;
    border-radius: 4px; /* Slightly rounded button in collapsed state */
    margin-left: 10px;
    white-space: nowrap; /* Prevent "发送" from wrapping */
  }

  /* Expanded Chat Box Specific Styles */
  #chat-expanded-box {
    display: flex; /* Stack header, messages, input vertically */
    flex-direction: column;
    position: fixed; /* Override wrapper's bottom:0 and align to full screen */
    top: 50px;
    bottom: 50px;
    left: 50%;
    transform: translateX(-50%); /* Center horizontally */
    width: 90%; /* Default width for PC */
    max-width: 600px; /* Max width for PC */
    background: white;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0,0,0,0.2); /* Deeper shadow for expanded state */
    overflow: hidden; /* Ensures content respects rounded corners */
    transition: all 0.3s ease-out; /* Smooth transition for expansion */
  }

  #chat-header {
    display: flex;
    justify-content: space-between; /* Align title left, close button right */
    align-items: center;
    padding: 10px 15px;
    background: #f4f6f8; /* Light gray from your site's feature background */
    border-bottom: 1px solid #e0e0e0; /* From your site's blockquote border */
    font-weight: bold;
    color: #2c3e50; /* Header color from your site's headings */
    font-size: 1.1em;
  }
  #chat-header button {
    background: none;
    border: none;
    color: #2c3e50; /* Match header text color */
    font-weight: bold;
    font-size: 1.2em;
    padding: 0 5px;
    line-height: 1;
  }

  #chat-messages {
    flex-grow: 1; /* Message area takes up most of the vertical space */
    overflow-y: auto; /* Enable scrolling for messages */
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background: #fcfcfc; /* Slightly off-white for message area */
  }

  .bot-message, .user-message {
    padding: 10px 12px;
    border-radius: 12px;
    max-width: 85%;
    word-wrap: break-word; /* Ensure long words break within the bubble */
    white-space: pre-wrap; /* Preserve whitespace and allow line breaks */
    line-height: 1.6;
  }
  .bot-message {
    background: #eef; /* Light blue from previous version */
    align-self: flex-start; /* Align bot messages to the left */
    color: #34495e; /* Default text color */
  }
  .user-message {
    background: #dcf8c6; /* Light green from previous version */
    align-self: flex-end; /* Align user messages to the right */
    color: #34495e;
  }
  /* Markdown styling within messages */
  .bot-message a, .user-message a {
    color: #3a77d8; /* Link color from your site */
    text-decoration: underline;
  }
  .bot-message strong, .user-message strong {
    font-weight: 700; /* Bold from your site */
  }
  /* Initial bot message style to push it to bottom if few messages */
  .bot-message.initial-message {
    margin-top: auto;
  }

  #chat-input-container {
    display: flex;
    border-top: 1px solid #e0e0e0; /* Match header border */
    padding: 10px 15px;
    background: #f4f6f8; /* Match header background */
  }
  #chat-input-expanded {
    flex-grow: 1;
    border: 1px solid #a8adac; /* From your site's input border */
    border-radius: 6px; /* Slightly rounded for the expanded input field */
    padding: 8px 12px;
    background: white;
  }
  #chat-input-expanded:focus {
    border-color: #3a77d8; /* Focus color from your site's links */
  }
  #chat-input-container button {
    margin-left: 10px;
    padding: 8px 18px;
    border-radius: 6px; /* Rounded buttons in expanded state */
  }

  /* Utility class to hide elements */
  .hidden {
    display: none !important;
  }

  /* Mobile responsiveness */
  @media (max-width: 768px) {
    #chat-ui-wrapper {
      right: 10px; /* Adjust right margin for smaller screens */
      left: 10px; /* Add left margin */
    }
    #chat-collapsed-input {
      width: calc(100% - 20px); /* Full width minus side margins */
      left: 10px;
      right: 10px;
      transform: translateY(-50px);
    }
    #chat-expanded-box {
      width: calc(100% - 20px); /* Almost full width minus side margins */
      top: 10px; /* Closer to top */
      bottom: 10px; /* Closer to bottom */
      max-width: none; /* Allow full mobile width */
      left: 10px;
      right: 10px;
      transform: none; /* No horizontal transform needed */
      border-radius: 5px; /* Slightly smaller border radius for mobile */
    }
    #chat-header, #chat-input-container {
      padding: 8px 10px; /* Adjust padding for mobile */
      font-size: 1em;
    }
    #chat-header button {
      font-size: 1.1em;
    }
    #chat-messages {
      padding: 10px;
      gap: 8px; /* Slightly smaller gap between messages */
    }
    .bot-message, .user-message {
      max-width: 90%; /* Slightly wider on mobile */
      padding: 8px 10px;
      font-size: 0.95rem; /* Slightly smaller font size */
    }
    #chat-input-expanded {
      padding: 6px 10px;
    }
    #chat-input-container button {
      padding: 6px 15px;
    }
  }
</style>

<!-- Calling Worker API JavaScript -->
<script>
  // --- Element References ---
  const chatUiWrapper = document.getElementById('chat-ui-wrapper');
  const chatCollapsedInput = document.getElementById('chat-collapsed-input');
  const chatInputCollapsed = document.getElementById('chat-input-collapsed');
  const chatSendCollapsed = document.getElementById('chat-send-collapsed');

  const chatExpandedBox = document.getElementById('chat-expanded-box');
  const chatCloseButton = document.getElementById('chat-close-button');
  const chatMessages = document.getElementById('chat-messages');
  const chatInputExpanded = document.getElementById('chat-input-expanded');
  const chatSendExpanded = document.getElementById('chat-send-expanded');

  // --- Configuration ---
  const WORKER_URL = 'https://proxy.true-dhamma.com/kb-chat'; // Your KB-Chat Worker URL

  // --- State Management ---
  let isChatExpanded = false;

  /**
   * Toggles the chat UI between collapsed and expanded states.
   * @param {boolean} expanded - True to expand, false to collapse.
   */
  function setChatState(expanded) {
    isChatExpanded = expanded;
    if (expanded) {
      chatCollapsedInput.classList.add('hidden');
      chatExpandedBox.classList.remove('hidden');
      chatInputExpanded.focus(); // Focus on the input in the expanded box
    } else {
      chatCollapsedInput.classList.remove('hidden');
      chatExpandedBox.classList.add('hidden');
      chatInputExpanded.value = ''; // Clear expanded input when collapsing
      chatInputCollapsed.focus(); // Focus on the collapsed input
    }
    scrollToBottom(); // Always scroll to bottom after state change
  }

  // --- Utility: Markdown Renderer (Lightweight and incremental for typing effect) ---
  // This renderer needs to be efficient as it runs on every character/interval.
  // It handles bold, links, and newlines. It avoids complex block-level parsing
  // during typing for performance, focusing on inline elements and line breaks.
  function renderPartialMarkdown(markdownText) {
    let html = markdownText;

    // Bold: **text** -> <strong>text</strong>
    // Needs to handle cases where ** is split, so non-greedy `*?`
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Links: [text](url) -> <a href="url" target="_blank">text</a>
    // Ensure relative URLs are handled correctly and target="_blank" for safety.
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (match, text, url) => {
        const target = url.startsWith('http') || url.startsWith('//') ? '_blank' : '_self';
        return `<a href="${url}" target="${target}">${text}</a>`;
    });
    
    // Convert newlines to <br> for simple line breaks within a message block.
    // This allows visual breaks during typing without complex paragraph reconstruction.
    html = html.replace(/\n/g, '<br>');

    return html;
  }

  // --- Typing Effect Function ---
  /**
   * Simulates typing a message into a given HTML element with Markdown rendering.
   * @param {HTMLElement} targetElement - The element to type into.
   * @param {string} fullText - The complete text to type.
   * @returns {Promise<void>} A promise that resolves when typing is complete.
   */
  async function typeMessage(targetElement, fullText) {
    targetElement.innerHTML = ''; // Clear existing content before typing
    let currentText = '';
    let charIndex = 0;
    const typingDelay = 25; // Milliseconds per character for typing speed
    const renderInterval = 5; // Re-render markdown every N characters to balance performance and visual effect

    return new Promise(resolve => {
      function typeChar() {
        if (charIndex < fullText.length) {
          currentText += fullText.charAt(charIndex);
          // Only re-render Markdown periodically or at the very end of the message
          if (charIndex % renderInterval === 0 || charIndex === fullText.length - 1) {
             targetElement.innerHTML = renderPartialMarkdown(currentText);
             scrollToBottom();
          }
          charIndex++;
          setTimeout(typeChar, typingDelay);
        } else {
          // Ensure final, complete Markdown rendering for the whole text
          targetElement.innerHTML = renderPartialMarkdown(fullText);
          scrollToBottom();
          resolve();
        }
      }
      typeChar(); // Start typing
    });
  }

  // --- Send Message Logic ---
  /**
   * Handles sending a user message, displaying it, calling the worker,
   * and displaying the bot's response with a typing effect.
   * @param {HTMLInputElement} inputElement - The input field where the query was typed.
   * @param {HTMLButtonElement} sendButton - The send button.
   */
  async function sendMessage(inputElement, sendButton) {
    const query = inputElement.value.trim();
    if (!query) return;

    // Display user's question
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'user-message';
    userMessageDiv.textContent = query;
    chatMessages.appendChild(userMessageDiv);
    scrollToBottom();

    // Clear input and disable send button
    inputElement.value = '';
    sendButton.disabled = true;
    sendButton.textContent = '思考中...';

    // Display a temporary thinking message from the bot
    const thinkingMessageDiv = document.createElement('div');
    thinkingMessageDiv.className = 'bot-message';
    thinkingMessageDiv.textContent = '思考中...'; // Initial text
    chatMessages.appendChild(thinkingMessageDiv);
    scrollToBottom();

    try {
      const response = await fetch(WORKER_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query })
      });

      if (!response.ok) {
        throw new Error(`API 请求失败: ${response.statusText}`);
      }

      const data = await response.json();
      // Replace the thinking message with the actual answer, using the typing effect
      await typeMessage(thinkingMessageDiv, data.answer);

    } catch (error) {
      // Display error message, also with Markdown rendering
      thinkingMessageDiv.innerHTML = renderPartialMarkdown('抱歉，服务出现了一点问题，请稍后再试。');
      console.error('Chat error:', error);
    } finally {
      // Re-enable send button and restore its text
      sendButton.disabled = false;
      sendButton.textContent = '发送';
      scrollToBottom(); // Ensure scroll to bottom after final message/error
    }
  }

  // --- Scroll to Bottom Utility ---
  function scrollToBottom() {
    // Smooth scroll if browser supports it
    chatMessages.scrollTo({
      top: chatMessages.scrollHeight,
      behavior: 'smooth'
    });
  }

  // --- Event Listeners ---

  // Collapsed input element interactions
  chatInputCollapsed.addEventListener('focus', () => setChatState(true));
  chatInputCollapsed.addEventListener('click', () => setChatState(true));
  chatSendCollapsed.addEventListener('click', () => {
    // Expand the chat first, then send the message from the expanded input
    setChatState(true);
    // Use a small timeout to allow UI to expand before sending
    setTimeout(() => {
      chatInputExpanded.value = chatInputCollapsed.value; // Transfer text
      sendMessage(chatInputExpanded, chatSendExpanded);
    }, 10);
  });
  chatInputCollapsed.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault(); // Prevent form submission or newline
      setChatState(true);
      setTimeout(() => {
        chatInputExpanded.value = chatInputCollapsed.value;
        sendMessage(chatInputExpanded, chatSendExpanded);
      }, 10);
    }
  });


  // Expanded chat close button
  chatCloseButton.addEventListener('click', () => setChatState(false));

  // Expanded chat input and send button interactions
  chatSendExpanded.addEventListener('click', () => sendMessage(chatInputExpanded, chatSendExpanded));
  chatInputExpanded.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && !event.shiftKey) { // Shift+Enter for multiline input
      event.preventDefault(); // Prevent newline in input
      sendMessage(chatInputExpanded, chatSendExpanded);
    }
  });

  // --- Initial Setup ---
  setChatState(false); // Start the chat in a collapsed state by default
</script>