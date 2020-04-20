from packages import request_lib as req

title = req.get_title("https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8")

print(title);