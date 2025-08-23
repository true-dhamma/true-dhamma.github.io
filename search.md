---
title: 搜索
excerpt: Search for a page or post you're looking for
---

{% include site-search.html %}

<!-- 聊天机器人界面 HTML -->
<div id="chat-container" style="position: fixed; bottom: 20px; right: 20px; width: 350px; border: 1px solid #ccc; border-radius: 10px; background: white; box-shadow: 0 0 10px rgba(0,0,0,0.1); font-family: sans-serif; display: flex; flex-direction: column;">
  <div id="chat-header" style="padding: 10px; background: #f1f1f1; border-bottom: 1px solid #ccc; font-weight: bold; border-top-left-radius: 10px; border-top-right-radius: 10px;">
    佛法问答
  </div>
  <div id="chat-messages" style="height: 300px; overflow-y: auto; padding: 10px; display: flex; flex-direction: column; gap: 10px;">
     <div class="bot-message" style="background: #eef; padding: 8px; border-radius: 8px; align-self: flex-start; max-width: 80%;">阿弥陀佛，请问有什么可以帮助您？</div>
  </div>
  <div id="chat-input-container" style="display: flex; border-top: 1px solid #ccc;">
    <input type="text" id="chat-input" placeholder="输入您的问题..." style="flex-grow: 1; border: none; padding: 10px; outline: none;">
    <button id="chat-submit" style="border: none; background: #007bff; color: white; padding: 10px 15px; cursor: pointer;">发送</button>
  </div>
</div>

<!-- 调用 Worker API 的 JavaScript -->
<script>
  const chatInput = document.getElementById('chat-input');
  const chatSubmit = document.getElementById('chat-submit');
  const chatMessages = document.getElementById('chat-messages');
  
  // 替换成你的 Worker URL
  const WORKER_URL = 'https://proxy.true-dhamma.com/kb-chat';

  async function askQuestion() {
    const query = chatInput.value.trim();
    if (!query) return;

    // 显示用户的问题
    const userMessageDiv = document.createElement('div');
    userMessageDiv.textContent = query;
    userMessageDiv.style.cssText = 'background: #dcf8c6; padding: 8px; border-radius: 8px; align-self: flex-end; max-width: 80%;';
    chatMessages.appendChild(userMessageDiv);
    
    chatInput.value = '';
    chatSubmit.disabled = true;
    chatSubmit.textContent = '思考中...';

    // 显示等待消息
    const thinkingMessageDiv = document.createElement('div');
    thinkingMessageDiv.textContent = '...';
    thinkingMessageDiv.style.cssText = 'background: #eef; padding: 8px; border-radius: 8px; align-self: flex-start; max-width: 80%;';
    chatMessages.appendChild(thinkingMessageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

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
      thinkingMessageDiv.textContent = data.answer; // 更新机器人回答

    } catch (error) {
      thinkingMessageDiv.textContent = '抱歉，服务出现了一点问题，请稍后再试。';
      console.error('Chat error:', error);
    } finally {
      chatSubmit.disabled = false;
      chatSubmit.textContent = '发送';
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }
  }

  chatSubmit.addEventListener('click', askQuestion);
  chatInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      askQuestion();
    }
  });
</script>