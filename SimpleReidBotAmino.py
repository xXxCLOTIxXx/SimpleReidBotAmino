import AminoLab
client = AminoLab.Client()
client.auth(email="gmail", password="password")
CHAT_CONST="chat_id"
NDC_CONST="id comunity"
old_messages = ["fmsg"]
oll = '!spam'
if oll == '!spam':
	client.send_message(ndc_Id=NDC_CONST, thread_Id=CHAT_CONST, message=';😀 😃 😄 😁 😆 😅 😂 🤣 😇 😉 😊 🙂 🙃 ☺ 😋 😌 😍 🥰 😘 😗 😙 😚 🥲 🤪 😜 😝 😛 🤑 😎 🤓 🥸 🧐 🤠 🥳 🤗 🤡 😏 😶 😐 😑 😒 🙄 🤨 🤔 🤫 🤭 🤥 😳 😞 😟 😠 😡 🤬 😔 😕 🙁 ☹', message_type=109)

old_messages = ["fmsg"]

while True:
	lst = client.get_thread_messages(ndc_Id=NDC_CONST, thread_Id=CHAT_CONST, size=1)['messageList']
	author_n = str(lst[0]['author']['nickname'])
	author_u = str(lst[0]['author']['uid'])
	content = lst[0]['content']
	if content == None:
		ct = "None"
	else:
		ct = lst[0]['content'].split(" ")
	time = lst[0]['createdTime']
	ndc = lst[0]['author']['ndcId']
	msg = lst[0]['messageId']
	thread = lst[0]['threadId']
	mtype = lst[0]['type']
	old_messages.append(msg)
	if old_messages[-2] == msg:
		pass
	else:
		print(f"\n{author_n}: {ct}")
		if ct[0][0] == ";":
			msg = content.replace(ct[0],"")
			client.send_message(ndc_Id=NDC_CONST, thread_Id=CHAT_CONST, message=';😀 😃 😄 😁 😆 😅 😂 🤣 😇 😉 😊 🙂 🙃 ☺ 😋 😌 😍 🥰 😘 😗 😙 😚 🥲 🤪 😜 😝 😛 🤑 😎 🤓 🥸 🧐 🤠 🥳 🤗 🤡 😏 😶 😐 😑 😒 🙄 🤨 🤔 🤫 🤭 🤥 😳 😞 😟 😠 😡 🤬 😔 😕 🙁 ☹', message_type=109)
