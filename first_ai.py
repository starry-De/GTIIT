import google.generativeai as genai

# 1. 拿出你的通行证 (请把下面这行替换成你刚才申请的真实 API Key)
GOOGLE_API_KEY = "AQ.Ab8RN6JLdSVHUO1RS3wKI0QQrg6f9Z3b5kt-c3_Tcm5vNiZAjA"
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 选择你要聊天的模型 (gemini-1.5-flash 速度快、性价比高，适合新手测试)
model = genai.GenerativeModel('gemini-2.5-flash')  # 你也可以试试 'gemini-3.5-flash' 或 'gemini-4.0-flash'，但它们可能更慢或更贵哦！

# 3. 构造并发送你的问题
print("正在等待 Gemini 回复...")
response = model.generate_content("你好，Gemini！我是个编程新手，请用幽默简短的一句话给我打个气。")

# 4. 打印它的回答
print("\nGemini 的回答：")
print(response.text)