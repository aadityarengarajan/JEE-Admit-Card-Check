import requests

breakable = False
while breakable ==False:
	if "admit card" in requests.get("https://jeemain.nta.nic.in/webinfo2021/Page/Page?PageId=1&LangId=P").text.lower():
		requests.get(f"https://api.callmebot.com/whatsapp.php?phone=+96599290755&text=*[JEE]]*\\n*_Admit Card Released. Please See https://jeemain.nta.nic.in_*&apikey=822832")
		requests.get("http://api.callmebot.com/start.php?source=auth&user=@arularx&text=Your+J+E+E+Admit+Card+has+been+released+Please+check+it+now.+Your+J+E+E+Admit+Card+has+been+released+Please+check+it+now.+This+is+an+automated+message+and+the+call+will+end+shortly.+Thank+You&lang=en-US-Standard-B&rpt=1")
		breakable = True
		break
		exit()
exit()