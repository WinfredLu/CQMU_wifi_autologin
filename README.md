该脚本通过调用WebDriver和Selenium软件包来执行JavaScript片段，以自动填充和登录重庆医科大学校园网认证页面。

校园网通过记录和比对联网设备mac地址来达到自动登录的效果。应用场景：mac地址经常变（出于合理的开发需要），又不想每次都输密码；有超过三台设备想交替联网的；其他……

WebDriver下载链接（Chrome）：https://googlechromelabs.github.io/chrome-for-testing/#stable

把wifi_login_activator.vbs修改之后放到启动文件夹里可以达到开机自动登录校园网的功能。对于Windows上单个用户来说，启动文件夹路径为AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup。
