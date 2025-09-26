---
title: 搜索&提问
excerpt: Search for a page or post's content
---

{% include site-search.html %}

<!-- 
  =============================================================
  Modern Chatbot UI v4.7.1 (CORS Bugfix)
  Author: Gemini Assistant & User
  Updates: 1. Corrected the WORKER_URL constant to include the proper
              /kb-chat path, fixing the critical CORS preflight error.
  =============================================================
-->

<!-- Chatbot FAB (Floating Action Button) -->
<div id="chat-fab-button" class="chat-fab-button">
  <svg class="chat-icon" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M21 6h-2v9H6v2c0 .55.45 1 1 1h11l4 4V7c0-.55-.45-1-1-1zm-4 6V4c0-.55-.45-1-1-1H3c-.55 0-1 .45-1 1v14l4-4h10c.55 0 1-.45 1-1z"/>
  </svg>
</div>

<!-- Chat Overlay and Modal Window -->
<div id="chat-overlay" class="chat-overlay hidden">
  <div id="chat-modal" class="chat-modal">
    <div class="chat-header">
      <button id="chat-new-button" class="chat-header-button" aria-label="新聊天">新聊天</button>
      <span class="chat-title">佛法问答</span>
      <button id="chat-close-button" class="chat-header-button" aria-label="关闭聊天">&times;</button>
    </div>
    <div id="chat-messages" class="chat-messages">
      <div class="message bot-message">
        <div class="message-content">请问有什么可以帮助您？</div>
      </div>
    </div>
    <div class="chat-input-area">
      <textarea id="chat-input" placeholder="输入您的问题..." rows="1" aria-label="输入聊天信息"></textarea>
      <button id="chat-submit-button" class="chat-submit-button" aria-label="发送">
        <svg id="send-icon" class="chat-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24px" height="24px"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
        <svg id="stop-icon" class="chat-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24px" height="24px" style="display: none;"><path d="M6 6h12v12H6z"/></svg>
      </button>
    </div>
  </div>
</div>

<!-- Dependencies -->
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.0.11/dist/purify.min.js"></script>

<style>
/* Base Styles */
.chat-fab-button, .chat-modal, .chat-modal * { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; box-sizing: border-box; line-height: 1.5; margin: 0; padding: 0; font-size: 19px; }
.chat-fab-button svg, .chat-submit-button svg { height: 24px; width: 24px; }
/* FAB */
.chat-fab-button { position: fixed; bottom: 30px; right: 30px; z-index: 1000; display: flex; justify-content: center; align-items: center; width: 56px; height: 56px; border: none; background-color: #3a77d8; color: #fff; border-radius: 50%; cursor: pointer; box-shadow: 0 6px 16px rgba(0,0,0,0.2); transition: all 0.2s ease-in-out; -webkit-tap-highlight-color: transparent; }
.chat-fab-button:hover { background-color: #2e60ad; transform: translateY(-2px); }
.chat-fab-button .chat-icon { fill: #fff; }
/* Overlay & Modal */
.chat-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(44, 62, 80, 0.6); z-index: 1100; display: flex; justify-content: center; align-items: center; opacity: 1; visibility: visible; transition: opacity 0.3s ease; }
.chat-overlay.hidden { visibility: hidden; opacity: 0; }
.chat-modal { background: #ffffff; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.2); display: flex; flex-direction: column; width: 90vw; height: 85vh; max-width: 700px; max-height: 800px; overflow: hidden; transform: scale(1); transition: transform 0.3s ease; }
.chat-overlay.hidden .chat-modal { transform: scale(0.95); }
/* Header */
.chat-header { background: #f4f6f8; color: #2c3e50; padding: 10px 15px; border-bottom: 1px solid #e0e0e0; display: flex; justify-content: space-between; align-items: center; flex-shrink: 0; position: relative; }
.chat-title { font-weight: 700; font-size: 1.1rem; position: absolute; left: 50%; transform: translateX(-50%); max-width: 60%; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.chat-header-button { background: none; border: none; cursor: pointer; font-size: 1rem; padding: 5px 8px; flex-shrink: 0; position: relative; z-index: 1; }
#chat-new-button { color: #3a77d8; font-weight: normal; text-decoration: none; }
#chat-new-button:hover { text-decoration: underline; }
#chat-close-button { font-size: 1.8rem; line-height: 1; padding: 0 5px; color: #2c3e50; }
/* Messages */
.chat-messages { flex-grow: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 14px; }
.chat-messages .message { max-width: 85%; padding: 12px 18px; border-radius: 18px; word-wrap: break-word; box-shadow: 0 1px 2px rgba(0,0,0,0.08); line-height: 1.6; }
.chat-messages .user-message { background: #EAEAEA; color: #2c3e50; align-self: flex-end; border-bottom-right-radius: 4px; }
.chat-messages .bot-message { background: #eaf2ff; align-self: flex-start; border-bottom-left-radius: 4px; }
/* Markdown & List Styles */
.message-content { color: #2c3e50; font-size: 1em; }
.message-content > *:first-child { margin-top: 0; } .message-content > *:last-child { margin-bottom: 0; }
.message-content p { margin: 0.5em 0; padding: 0; } .message-content a { color: #3a77d8; text-decoration: underline; cursor: pointer; }
.message-content ul, .message-content ol { margin-top: 1em; margin-bottom: 1em; padding-left: 40px; }
.message-content li { display: list-item; margin-bottom: 0.5em; }
.message-content sup a {
  font-size: 0.75em;      /* 字体缩小为正常大小的 75% */
  vertical-align: super;  /* 确保上标对齐 */
  text-decoration: none;  /* 去掉下划线，让它更像一个引用标记 */
  padding: 0 2px;         /* 稍微增加一点内边距，避免拥挤 */
}
/* Input Area */
.chat-input-area { display: flex; align-items: flex-end; padding: 12px 15px; border-top: 1px solid #e0e0e0; background: #fff; flex-shrink: 0; gap: 10px; }
.chat-input-area textarea { flex-grow: 1; border: 1px solid #ccc; border-radius: 22px; padding: 8px 18px; resize: none; max-height: 120px; outline: none; transition: border-color 0.2s ease; -webkit-appearance: none; font-size: 18px; }
.chat-input-area textarea:focus { border-color: #3a77d8; }
.chat-submit-button { background: #3a77d8; border: none; border-radius: 50%; width: 44px; height: 44px; cursor: pointer; flex-shrink: 0; display: flex; justify-content: center; align-items: center; transition: all 0.2s ease; color: white; -webkit-tap-highlight-color: transparent; }
.chat-submit-button:hover:not(:disabled) { background-color: #2e60ad; }
.chat-submit-button:disabled { background-color: #a8adac; cursor: not-allowed; }
.chat-submit-button .chat-icon { fill: currentColor; }
/* Mobile */
@media (max-width: 768px) {
    .chat-modal { width: 100%; height: 100%; max-width: 100vw; max-height: 100vh; border-radius: 0; }
    .chat-modal, .chat-modal * { font-size: 18px; }
    .chat-input-area textarea { font-size: 16px; padding: 10px 18px; }
    .chat-header { padding: 10px; }
    .chat-title { font-size: 1em; }
    .chat-header-button { font-size: 1em; }
}
</style>
<script>
document.addEventListener('DOMContentLoaded', () => {
    // --- Configuration ---
    // CORRECTED URL
    const WORKER_URL = 'https://proxy.true-dhamma.com/kb-chat';
    const MAX_HISTORY_TURNS = 5;

    // --- State Management & DOM Elements ---
    let fetchController = null;
    let typingInterval = null;
    let chatHistory = []; 
    const chatFabButton = document.getElementById('chat-fab-button');
    const chatOverlay = document.getElementById('chat-overlay');
    const chatCloseButton = document.getElementById('chat-close-button');
    const chatNewButton = document.getElementById('chat-new-button'); 
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const chatSubmitButton = document.getElementById('chat-submit-button');
    const sendIcon = document.getElementById('send-icon');
    const stopIcon = document.getElementById('stop-icon');
    const renderer = new marked.Renderer();
    renderer.link = (href, title, text) => `<a href="${href}" title="${title || ''}" target="_blank" rel="noopener noreferrer">${text}</a>`;
    marked.setOptions({ renderer: renderer, gfm: true, breaks: true });
    const sanitize = DOMPurify.sanitize;
    const openChat = () => { document.body.style.overflow = 'hidden'; chatOverlay.classList.remove('hidden'); setTimeout(() => chatInput.focus(), 300); };
    const closeChat = () => { stopFetchingAndTyping(); chatOverlay.classList.add('hidden'); setTimeout(() => { document.body.style.overflow = ''; }, 300); };
    const startNewChat = () => { stopFetchingAndTyping(); chatHistory = []; chatMessages.innerHTML = `<div class="message bot-message"><div class="message-content">您好，新的对话已经开始。请问有什么可以帮助您？</div></div>`; chatInput.focus(); };
    const setButtonState = (state) => {
        const isThinking = state === 'thinking';
        chatInput.disabled = isThinking;
        chatSubmitButton.disabled = false;
        chatSubmitButton.setAttribute('aria-label', isThinking ? '停止' : '发送');
        sendIcon.style.display = isThinking ? 'none' : 'block';
        stopIcon.style.display = isThinking ? 'block' : 'none';
        if (!isThinking) chatInput.focus();
    };
    const typeMessage = (messageElement, fullMarkdown, delay = 15) => {
        return new Promise((resolve) => {
            if (typingInterval) clearInterval(typingInterval);
            let currentMarkdown = '', charIndex = 0;
            typingInterval = setInterval(() => {
                if (charIndex < fullMarkdown.length) {
                    currentMarkdown += fullMarkdown[charIndex++];
                    messageElement.innerHTML = sanitize(marked.parse(currentMarkdown));
                    chatMessages.scrollTop = chatMessages.scrollHeight;
                } else {
                    clearInterval(typingInterval);
                    typingInterval = null;
                    resolve();
                }
            }, delay);
        });
    };
    const stopFetchingAndTyping = () => { if (fetchController) fetchController.abort(); if (typingInterval) clearInterval(typingInterval); setButtonState('idle'); };

    // --- sendMessage function with link rendering fix ---
    const sendMessage = async () => {
        const query = chatInput.value.trim();
        if (!query) return;

        stopFetchingAndTyping();
        
        const userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'message user-message';
        userMessageDiv.innerHTML = `<div class="message-content">${query.replace(/</g, "&lt;").replace(/>/g, "&gt;")}</div>`;
        chatMessages.appendChild(userMessageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        chatInput.value = '';
        chatInput.style.height = 'auto';
        setButtonState('thinking');

        const botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'message bot-message';
        const botMessageContent = document.createElement('div');
        botMessageContent.className = 'message-content';
        botMessageDiv.appendChild(botMessageContent);
        chatMessages.appendChild(botMessageDiv);
        
        try {
            fetchController = new AbortController();
            const historyToSend = chatHistory.slice(-MAX_HISTORY_TURNS * 2);
            const response = await fetch(WORKER_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query, history: historyToSend }),
                signal: fetchController.signal
            });

            if (!response.ok) throw new Error(`API 请求失败: ${response.statusText}`);

            const data = await response.json();
            
            const sourceSeparator = "\n\n\n**相关内容出自：**";
            let mainAnswer = data.answer;
            let sourcePart = "";

            const separatorIndex = data.answer.indexOf(sourceSeparator);
            if (separatorIndex !== -1) {
                mainAnswer = data.answer.substring(0, separatorIndex);
                sourcePart = data.answer.substring(separatorIndex);
            }

            await typeMessage(botMessageContent, mainAnswer);

            if (sourcePart) {
                const existingHTML = botMessageContent.innerHTML;
                const sourceHTML = sanitize(marked.parse(sourcePart));
                botMessageContent.innerHTML = existingHTML + sourceHTML;
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }

            chatHistory.push({ role: 'user', parts: [{ text: query }] });
            chatHistory.push({ role: 'model', parts: [{ text: mainAnswer }] }); // 只将纯净的回答存入历史

        } catch (error) {
            if (error.name === 'AbortError') {
                botMessageContent.textContent = '已停止。';
            } else {
                console.error('Chat error:', error);
                botMessageContent.innerHTML = sanitize(marked.parse('抱歉，服务出现了一点问题，请稍后再试。'));
            }
        } finally {
            if (fetchController && !fetchController.signal.aborted) {
                setButtonState('idle');
            }
            fetchController = null;
        }
    };

    // --- Event Listeners ---
    chatFabButton.addEventListener('click', openChat);
    chatCloseButton.addEventListener('click', closeChat);
    chatNewButton.addEventListener('click', startNewChat); 
    chatOverlay.addEventListener('click', (e) => { if (e.target === chatOverlay) closeChat(); });
    chatMessages.addEventListener('click', (event) => {
        const link = event.target.closest('a');
        if (link && link.href) {
            event.preventDefault();
            window.open(link.href, '_blank', 'noopener,noreferrer');
        }
    });
    chatSubmitButton.addEventListener('click', () => { (stopIcon.style.display === 'block') ? stopFetchingAndTyping() : sendMessage(); });
    chatInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey && !e.isComposing) {
            e.preventDefault();
            sendMessage();
        }
    });
    chatInput.addEventListener('input', () => { chatInput.style.height = 'auto'; chatInput.style.height = `${chatInput.scrollHeight}px`; });
});
</script>