---
title: 搜索
excerpt: Search for a page or post you're looking for
---

{% include site-search.html %}

<!-- Chatbot FAB (Mobile Only / Toggle) -->
<div class="kb-chat-fab-container" id="kb-chat-fab-container">
  <button id="kb-chat-toggle-fab" class="kb-chat-fab-button" aria-label="打开/关闭佛法问答机器人">
    <svg class="kb-chat-icon" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#FFFFFF">
      <path d="M0 0h24v24H0V0z" fill="none"/><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/>
    </svg>
  </button>
</div>

<!-- Initial Input Bar (PC default, hidden on mobile until FAB clicked) -->
<div id="kb-chat-initial-input" class="kb-chat-initial-input-container">
  <input type="text" id="kb-chat-input-initial" placeholder="提问佛法，获取智慧解答..." autocomplete="off" />
  <button id="kb-chat-send-initial" class="kb-chat-send-btn">
    <svg class="kb-chat-icon" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="currentColor">
      <path d="M0 0h24v24H0V0z" fill="none"/><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2 .01 7z"/>
    </svg>
  </button>
</div>

<!-- Full Chat Window -->
<div id="kb-chat-full-window" class="kb-chat-full-window">
  <div class="kb-chat-header">
    佛法问答
    <button id="kb-chat-close-full" class="kb-chat-close-btn" aria-label="关闭聊天窗口">
      <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#FFFFFF">
        <path d="M0 0h24v24H0V0z" fill="none"/><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
      </svg>
    </button>
  </div>
  <div id="kb-chat-messages-full" class="kb-chat-messages">
    <!-- Messages will be appended here -->
  </div>
  <div class="kb-chat-input-container">
    <input type="text" id="kb-chat-input-full" placeholder="输入您的问题..." autocomplete="off" />
    <button id="kb-chat-send-full" class="kb-chat-send-btn">
      <svg class="kb-chat-icon" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="currentColor">
        <path d="M0 0h24v24H0V0z" fill="none"/><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2 .01 7z"/>
      </svg>
    </button>
  </div>
</div>

<style>
  /* Base styles for existing page elements - for reference on reuse */
  body {
    font-family: "Palatino", "Apple Garamond", Georgia, "Songti SC", "SimSun", "FangSong", serif;
    color: #34495e; /* Existing body text color */
  }
  a {
    color: #3a77d8; /* Existing link color */
  }
  .button, input[type=submit] {
    background: #3a77d8; /* Existing button color */
    color: #fff;
  }
  input[type=text], input[type=email], input[type=search], textarea, select {
    border: 1px solid #a8adac; /* Existing input border color */
  }
  input[type=text]:focus, input[type=email]:focus, input[type=search]:focus, textarea:focus, select:focus {
    outline: solid .12rem #fa407a; /* Existing focus outline */
  }

  /* Chatbot Specific Styles - Flat Design with Square Corners */

  /* FAB Container */
  .kb-chat-fab-container {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 1000;
  }

  /* FAB Button */
  .kb-chat-fab-button {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 56px;
    height: 56px;
    border: none;
    background-color: #3a77d8; /* Primary blue from site links */
    border-radius: 0; /* Square corners */
    cursor: pointer;
    padding: 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    transition: background-color 0.2s ease-in-out, transform 0.2s ease;
  }
  .kb-chat-fab-button:hover {
    background-color: #2e60ad; /* Darker blue on hover */
    transform: translateY(-2px);
  }
  .kb-chat-fab-button:active {
    transform: scale(0.95);
  }
  .kb-chat-fab-button .kb-chat-icon {
    fill: white;
    width: 28px;
    height: 28px;
  }

  /* Initial Input Bar (PC default) */
  .kb-chat-initial-input-container {
    position: fixed;
    bottom: 0; /* Position at the very bottom */
    left: 0;
    width: 100%;
    padding: 10px 20px; /* Some padding */
    background-color: #fff;
    border-top: 1px solid #e0e0e0; /* Subtle top border */
    box-shadow: 0 -2px 10px rgba(0,0,0,0.05); /* Subtle shadow */
    display: flex;
    align-items: center;
    z-index: 990; /* Below FAB, above page content */
    transition: all 0.3s ease-in-out;
    visibility: hidden; /* Controlled by JS */
    opacity: 0; /* Controlled by JS */
    transform: translateY(100%); /* Start off-screen */
  }
  .kb-chat-initial-input-container.visible {
    visibility: visible;
    opacity: 1;
    transform: translateY(0);
  }

  #kb-chat-input-initial {
    flex-grow: 1;
    border: 1px solid #a8adac; /* Reuse page input border */
    border-radius: 0; /* Square corners */
    padding: 10px 15px;
    outline: none;
    font-size: 1em;
    margin-right: 10px;
    background-color: #fff;
    color: #34495e;
  }
  #kb-chat-input-initial:focus {
    border-color: #fa407a; /* Reuse page focus color */
    outline: none; /* remove default browser outline */
  }

  /* Send Button for both initial bar and full window */
  .kb-chat-send-btn {
    background-color: #3a77d8; /* Reuse primary blue */
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 0; /* Square corners */
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.2s ease;
  }
  .kb-chat-send-btn:hover {
    background-color: #2e60ad;
  }
  .kb-chat-send-btn:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  .kb-chat-send-btn svg {
    width: 20px;
    height: 20px;
    fill: white;
  }

  /* Full Chat Window */
  .kb-chat-full-window {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80vw; /* Occupy most width */
    height: 80vh; /* Occupy most height */
    max-width: 900px; /* Max width for large screens */
    max-height: 700px; /* Max height */
    border-radius: 0; /* Square corners */
    background: #fff;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    font-family: inherit; /* Inherit font from page */
    color: inherit; /* Inherit color from page */
    z-index: 1000;
    transition: all 0.3s ease-in-out;
    visibility: hidden;
    opacity: 0;
    transform: translate(-50%, -45%) scale(0.95); /* Initial slightly off-center and scaled for animation */
  }
  .kb-chat-full-window.visible {
    visibility: visible;
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
  /* Overlay for full window */
  .kb-chat-full-window-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.4);
    z-index: 999;
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
  }
  .kb-chat-full-window-overlay.visible {
    visibility: visible;
    opacity: 1;
  }


  /* Header for full window */
  .kb-chat-header {
    background-color: #607D8B; /* Soft blue-grey */
    color: white;
    padding: 15px 20px;
    font-size: 1.1em;
    font-weight: 500;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #455A64; /* Darker border */
    border-radius: 0; /* Square corners */
  }
  .kb-chat-close-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding: 5px;
  }
  .kb-chat-close-btn svg {
    fill: white;
    width: 20px;
    height: 20px;
  }
  .kb-chat-close-btn:hover svg {
    fill: #e0e0e0;
  }

  /* Messages Container */
  .kb-chat-messages {
    flex-grow: 1;
    overflow-y: auto;
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background-color: #f8f8f8; /* Light background for messages */
  }
  /* Scrollbar styles - reuse if available or define simple */
  .kb-chat-messages::-webkit-scrollbar { width: 8px; }
  .kb-chat-messages::-webkit-scrollbar-track { background: #f1f1f1; }
  .kb-chat-messages::-webkit-scrollbar-thumb { background: #bbb; }
  .kb-chat-messages::-webkit-scrollbar-thumb:hover { background: #888; }


  /* Message Bubbles */
  .kb-message {
    padding: 10px 15px;
    border-radius: 0; /* Square corners */
    max-width: 85%; /* Slightly wider messages */
    word-wrap: break-word;
    line-height: 1.5;
    font-size: 0.95em;
    position: relative; /* For typing cursor */
  }
  .kb-message--bot {
    background: #e0e0e0; /* Light grey for bot */
    color: inherit; /* Inherit from page */
    align-self: flex-start;
  }
  .kb-message--user {
    background: #e0f2f7; /* Soft blue for user */
    color: inherit;
    align-self: flex-end;
  }
  /* Markdown specific styles within messages - reuse .typeset where possible */
  .kb-message strong, .kb-message b { font-weight: 700; } /* Matches .typeset b, .typeset strong */
  .kb-message em, .kb-message i { font-style: italic; } /* Matches .typeset em, .typeset i */
  .kb-message a {
    color: #3a77d8; /* Matches page link color */
    text-decoration: underline;
  }
  .kb-message--user a {
    color: #2e60ad; /* Slightly darker for contrast on user bubble */
  }
  .kb-message ul, .kb-message ol { padding-left: 20px; margin: 5px 0; }
  .kb-message li { margin-bottom: 5px; }
  .kb-message pre {
    background-color: #eee;
    padding: 8px;
    border-radius: 0; /* Square corners */
    font-family: 'Fira Code', 'SF Mono', monospace;
    font-size: 0.85em;
    white-space: pre-wrap;
    word-break: break-all;
    overflow-x: auto;
  }
  .kb-message code {
    background-color: #e0e0e0;
    padding: 2px 4px;
    border-radius: 0; /* Square corners */
    font-family: 'Fira Code', 'SF Mono', monospace;
    font-size: 0.85em;
  }
  /* For footnote style sources section */
  .kb-message .sources-section {
    font-size: 0.8em;
    margin-top: 15px;
    padding-top: 10px;
    border-top: 1px solid #ddd;
    color: #666;
  }
  .kb-message .sources-section strong {
    color: #333;
  }
  .kb-message .sources-section ol {
    list-style-type: decimal;
    padding-left: 20px;
    margin-top: 5px;
  }
  .kb-message .sources-section ol li {
    margin-bottom: 3px;
  }

  /* Input Container for full window */
  .kb-chat-full-window .kb-chat-input-container {
    display: flex;
    padding: 10px 15px;
    border-top: 1px solid #eee;
    background-color: #fff;
    border-radius: 0; /* Square corners */
  }
  #kb-chat-input-full {
    flex-grow: 1;
    border: 1px solid #a8adac; /* Reuse page input border */
    border-radius: 0; /* Square corners */
    padding: 10px 15px;
    outline: none;
    font-size: 1em;
    margin-right: 10px;
    background-color: #fff;
    color: #34495e;
  }
  #kb-chat-input-full:focus {
    border-color: #fa407a; /* Reuse page focus color */
    outline: none;
  }

  /* Typing cursor */
  .kb-typing-cursor {
    display: inline-block;
    width: 2px;
    height: 1em; /* Adjust height to match text line height */
    background-color: #333; /* Color of the cursor */
    vertical-align: middle;
    margin-left: 2px;
    animation: blink-caret 0.75s step-end infinite;
  }
  @keyframes blink-caret {
    from, to { background-color: transparent }
    50% { background-color: #333 }
  }


  /* Media Queries for Responsiveness */
  @media (max-width: 768px) {
    .kb-chat-full-window {
      width: 95vw; /* Almost full width */
      height: 90vh; /* Almost full height */
      /* No transform from initial for mobile, it always opens from FAB */
      transform: translate(-50%, -50%); 
    }
    .kb-chat-initial-input-container {
      display: none !important; /* Hide initial input bar on mobile */
      visibility: hidden !important;
      opacity: 0 !important;
    }
    .kb-chat-fab-container {
      display: block; /* Show FAB on mobile */
    }
  }

  @media (min-width: 769px) {
    .kb-chat-fab-container {
      display: none !important; /* Hide FAB on PC */
    }
    .kb-chat-initial-input-container {
      bottom: 50px; /* Adjust as per requirement - 50px from bottom */
    }
  }
</style>

<script>
  // Utility to render basic Markdown to HTML
  function renderMarkdown(markdownText) {
    if (!markdownText) return '';

    let html = markdownText;

    // Convert bold: **text** or __text__ to <strong>text</strong>
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/__([^_]+)__/g, '<strong>$1</strong>');

    // Convert italics: *text* or _text_ to <em>$1</em>
    html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');
    html = html.replace(/_([^_]+)_/g, '<em>$1</em>');

    // Convert links: [text](url) to <a href="url" target="_blank" rel="noopener noreferrer">text</a>
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

    // Convert code blocks (multiline)
    html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    // Convert inline code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Handle paragraphs and lists
    // Split by double newline to treat blocks separately.
    const blocks = html.split(/\n\n+/); 

    let processedHtml = blocks.map(block => {
        // Check for lists at the start of a block
        if (block.match(/^\d+\.\s/) || block.match(/^\s*[-*+]\s/)) {
            // If it's the "**相关内容出自：**" section, wrap it in a div for specific styling
            if (block.startsWith('**相关内容出自：**')) {
                const sourcesContent = block.substring('**相关内容出自：**'.length).trim();
                const listItems = sourcesContent.split('\n').filter(line => line.trim() !== '').map(item => {
                    // Item could be "1. [Title](URL)"
                    // Keep the number, but remove any extra spaces, then render link.
                    const match = item.match(/^(\d+\.\s*)(.*)$/);
                    if (match) {
                        return `<li>${match[1]}${renderMarkdown(match[2].trim())}</li>`;
                    }
                    return `<li>${renderMarkdown(item.trim())}</li>`; // Fallback for unexpected formats
                }).join('');
                return `<div class="sources-section"><strong>相关内容出自：</strong><ol>${listItems}</ol></div>`;
            } else if (block.match(/^\d+\.\s/)) { // Generic ordered list
                const items = block.split('\n').filter(line => line.match(/^\d+\.\s/)).map(item => `<li>${item.replace(/^\d+\.\s/, '').trim()}</li>`).join('');
                return `<ol>${items}</ol>`;
            } else { // Generic unordered list
                const items = block.split('\n').filter(line => line.match(/^\s*[-*+]\s/)).map(item => `<li>${item.replace(/^\s*[-*+]\s/, '').trim()}</li>`).join('');
                return `<ul>${items}</ul>`;
            }
        } 
        // For other blocks, treat as paragraphs and convert single newlines to <br>
        else {
            return `<p>${block.replace(/\n/g, '<br>')}</p>`;
        }
    }).join('');

    // Remove any empty <p> tags that might result from parsing
    processedHtml = processedHtml.replace(/<p><\/p>/g, '');
    
    return processedHtml;
  }

  // --- DOM Elements ---
  const kbChatFabContainer = document.getElementById('kb-chat-fab-container');
  const kbChatToggleFab = document.getElementById('kb-chat-toggle-fab');
  
  const kbChatInitialInputContainer = document.getElementById('kb-chat-initial-input');
  const kbChatInputInitial = document.getElementById('kb-chat-input-initial');
  const kbChatSendInitial = document.getElementById('kb-chat-send-initial');

  const kbChatFullWindow = document.getElementById('kb-chat-full-window');
  const kbChatCloseFull = document.getElementById('kb-chat-close-full');
  const kbChatMessagesFull = document.getElementById('kb-chat-messages-full');
  const kbChatInputFull = document.getElementById('kb-chat-input-full');
  const kbChatSendFull = document.getElementById('kb-chat-send-full');

  // Create an overlay for the full chat window (added to body in HTML for cleaner structure)
  const overlay = document.querySelector('.kb-chat-full-window-overlay');

  const CHAT_WORKER_URL = 'https://proxy.true-dhamma.com/kb-chat';
  const TYPING_SPEED = 30; // Milliseconds per character
  const TYPING_CHUNK_SIZE = 2; // How many characters to type at once (for faster feeling)

  // --- State Variables ---
  let isMobileDevice = window.innerWidth <= 768; // Initial check
  let isFullChatWindowVisible = false;

  // --- Utility Functions ---
  const saveChatState = () => {
    localStorage.setItem('kbChatFullWindowVisible', isFullChatWindowVisible);
  };

  const setFullChatWindowVisibility = (visible) => {
    isFullChatWindowVisible = visible;
    if (visible) {
      kbChatFullWindow.classList.add('visible');
      overlay.classList.add('visible');
      kbChatInputFull.focus();
    } else {
      kbChatFullWindow.classList.remove('visible');
      overlay.classList.remove('visible');
    }
    saveChatState();
  };

  const showInitialInputBar = (visible) => {
    if (visible) {
      kbChatInitialInputContainer.classList.add('visible');
      kbChatInputInitial.focus();
    } else {
      kbChatInitialInputContainer.classList.remove('visible');
    }
  };

  const showFabButton = (visible) => {
    if (visible) {
      kbChatFabContainer.style.display = 'block';
    } else {
      kbChatFabContainer.style.display = 'none';
    }
  };

  const initializeChatUI = () => {
    isMobileDevice = window.innerWidth <= 768; // Re-evaluate on init/resize
    const savedState = localStorage.getItem('kbChatFullWindowVisible');

    if (savedState !== null) {
      isFullChatWindowVisible = (savedState === 'true'); // localStorage stores strings
    } else {
      // Default: PC shows input bar (which can expand), mobile shows FAB (closed)
      isFullChatWindowVisible = false; // Always start with full window closed, then determine how to trigger it
    }

    if (isMobileDevice) {
      showFabButton(true);
      showInitialInputBar(false);
      setFullChatWindowVisibility(false); // Mobile always starts with FAB, full window closed
    } else {
      showFabButton(false);
      // On PC, if user previously had full chat open, reopen it. Otherwise, show initial input bar.
      if (isFullChatWindowVisible) {
        showInitialInputBar(false);
        setFullChatWindowVisibility(true);
      } else {
        showInitialInputBar(true); // PC default: initial input bar visible
        setFullChatWindowVisibility(false);
      }
    }
  };

  const typeWriter = (element, text, typingCursorElement, onComplete) => {
    let i = 0;
    const interval = setInterval(() => {
      if (i < text.length) {
        const currentPartialText = text.substring(0, i + TYPING_CHUNK_SIZE);
        element.innerHTML = renderMarkdown(currentPartialText);
        element.appendChild(typingCursorElement); // Keep cursor at the end
        // Scroll parent if it's scrollable and cursor is near bottom
        if (element.parentElement) {
            const container = element.parentElement;
            if (container.scrollHeight - container.scrollTop - container.clientHeight < 50) { // If close to bottom
                container.scrollTop = container.scrollHeight;
            }
        }
        i += TYPING_CHUNK_SIZE;
      } else {
        clearInterval(interval);
        if (typingCursorElement && typingCursorElement.parentElement) {
          typingCursorElement.remove(); // Remove cursor after typing
        }
        element.innerHTML = renderMarkdown(text); // Final render after all text
        if (element.parentElement) {
            element.parentElement.scrollTop = element.parentElement.scrollHeight; // Final scroll
        }
        if (typeof onComplete === 'function') {
          onComplete();
        }
      }
    }, TYPING_SPEED);
  };

  const addMessageWithTyping = (text, sender, targetContainer) => {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('kb-message');
    messageDiv.classList.add(`kb-message--${sender}`);
    
    const contentSpan = document.createElement('div'); // Use div for block-level markdown elements like lists/code
    messageDiv.appendChild(contentSpan);

    const typingCursor = document.createElement('span'); // Cursor element
    typingCursor.classList.add('kb-typing-cursor');
    messageDiv.appendChild(typingCursor); // Add cursor initially

    targetContainer.appendChild(messageDiv);
    targetContainer.scrollTop = targetContainer.scrollHeight;

    return new Promise(resolve => {
        typeWriter(contentSpan, text, typingCursor, resolve);
    });
  };

  const sendQuestion = async (query, inputElement, sendButtonElement, messagesContainer) => {
    if (!query) return;

    // Add user message immediately
    await addMessageWithTyping(query, 'user', messagesContainer);
    inputElement.value = '';
    inputElement.disabled = true;
    sendButtonElement.disabled = true;

    // Show "思考中" with typing effect
    const thinkingMessagePromise = addMessageWithTyping('思考中', 'bot', messagesContainer); 
    
    try {
      const response = await fetch(CHAT_WORKER_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query })
      });

      if (!response.ok) {
        throw new Error(`API 请求失败: ${response.statusText}`);
      }

      const data = await response.json();
      await thinkingMessagePromise; // Wait for "思考中" to finish typing
      messagesContainer.lastChild.remove(); // Remove "思考中" placeholder
      
      await addMessageWithTyping(data.answer, 'bot', messagesContainer); // Type out the actual answer

    } catch (error) {
      console.error('Chat error:', error);
      await thinkingMessagePromise; // Wait for "思考中" to finish typing
      messagesContainer.lastChild.remove(); // Remove "思考中" placeholder
      await addMessageWithTyping('抱歉，服务出现了一点问题，请稍后再试。', 'bot', messagesContainer);
    } finally {
      inputElement.disabled = false;
      sendButtonElement.disabled = false;
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
      inputElement.focus();
    }
  };


  // --- Event Listeners ---
  kbChatToggleFab.addEventListener('click', () => {
    setFullChatWindowVisibility(!isFullChatWindowVisible);
  });

  kbChatCloseFull.addEventListener('click', () => {
    setFullChatWindowVisibility(false);
    // On PC, if full chat is closed, revert to initial input bar
    if (!isMobileDevice) {
      showInitialInputBar(true);
    }
  });

  // PC: Initial input bar focus/keydown
  kbChatInputInitial.addEventListener('focus', () => {
    setFullChatWindowVisibility(true);
    showInitialInputBar(false);
    // Transfer text from initial input to full chat input
    kbChatInputFull.value = kbChatInputInitial.value;
  });

  kbChatSendInitial.addEventListener('click', () => {
    // If user sends from initial bar, open full window and send
    setFullChatWindowVisibility(true);
    showInitialInputBar(false);
    sendQuestion(kbChatInputInitial.value, kbChatInputFull, kbChatSendFull, kbChatMessagesFull);
    kbChatInputInitial.value = ''; // Clear initial input
  });
  kbChatInputInitial.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      setFullChatWindowVisibility(true);
      showInitialInputBar(false);
      sendQuestion(kbChatInputInitial.value, kbChatInputFull, kbChatSendFull, kbChatMessagesFull);
      kbChatInputInitial.value = ''; // Clear initial input
    }
  });


  // Full chat window input/send
  kbChatSendFull.addEventListener('click', () => sendQuestion(kbChatInputFull.value, kbChatInputFull, kbChatSendFull, kbChatMessagesFull));
  kbChatInputFull.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      sendQuestion(kbChatInputFull.value, kbChatInputFull, kbChatSendFull, kbChatMessagesFull);
    }
  });

  // Handle window resize for responsiveness
  window.addEventListener('resize', () => {
    // Re-initialize UI based on new window size, but keep current chat open state if possible
    const wasFullChatOpen = isFullChatWindowVisible; // Store current state
    initializeChatUI(); // Re-apply visibility based on device type
    if (wasFullChatOpen) { // If it was open, try to keep it open
        setFullChatWindowVisibility(true);
    }
  });

  // --- Initial Page Load ---
  document.addEventListener('DOMContentLoaded', async () => {
    initializeChatUI();
    // Add initial bot greeting message with typing effect to full chat window
    await addMessageWithTyping('阿弥陀佛，请问有什么可以帮助您？', 'bot', kbChatMessagesFull);
  });
</script>