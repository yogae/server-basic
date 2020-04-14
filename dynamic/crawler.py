from packages import request_lib as req

title = req.get_title("http://web-static-hosting-bucket.s3-website.ap-northeast-2.amazonaws.com")

print(title);