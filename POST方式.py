Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> values={}
>>> values = {"username":"2915912248@qq.com","password":"XXXX"}
>>> data = urllib.urlencode(values)
>>> url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
>>> request = urllib2.Request(url,data)
>>> response = urllib2.urlopen(request)
>>> print response.read(3000)







<html>
  <head>
    <meta charset="utf-8" />
    <meta name="referrer" content="unsafe-url">
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta property="qc:admins" content="24530273213633466654" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>帐号登录</title>
    
    
    <link type="text/css" rel="stylesheet" href="/css/bootstrap.css;jsessionid=2DF4474FF68A230CA324392395F4EEE6.tomcat2" />
    <link type="text/css" rel="stylesheet" href="/css/login.css;jsessionid=2DF4474FF68A230CA324392395F4EEE6.tomcat2" />
    <link type="text/css" rel="stylesheet" href="/css/weixinqr.css;jsessionid=2DF4474FF68A230CA324392395F4EEE6.tomcat2" />
    <script src="https://res.wx.qq.com/connect/zh_CN/htmledition/js/wxLogin.js"></script>
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <script>
	var _hmt = _hmt || [];
	(function() {
	  var hm = document.createElement("script");
	  hm.src = "https://hm.baidu.com/hm.js?6bcd52f51e9b3dce32bec4a3997715ac";
	  var s = document.getElementsByTagName("script")[0]; 
	  s.parentNode.insertBefore(hm, s);
	})();
	</script>
  </head>
  <body>
  	<div id="hidebg"></div>
	<div id="hidebox"><div id="close" onClick="hide();"></div><div id="wxqr" class="wxqr"></div></div>
  	<script type="text/javascript">
  		var protocol = window.location.protocol;
  		document.write('<script type="text/javascript" src="' +protocol+ '//csdnimg.cn/pubfooter/js/repoAddr2.js?v=' + Math.random() + '"></'+'script>');
	</script>
	
    <div class="header"></div>
    <div class="main" style="background:url(https://csdnimg.cn/passport/login-bg.png)">
      <div class="container container-custom">
        <div class="row wrap-login">
          <div class="login-banner col-sm-6 col-md-7 col-lg-7 hidden-xs"><a href="http://dwz.cn/6JIiAl" target="_blank"><img src=https://csdnimg.cn/passport/login-banner.png class="img-responsive"></a></div>
          <div class="login-user col-xs-12 col-sm-6 col-md-5 col-lg-5">
            <div class="login-part">
              <h3>帐号登录 </h3>
              <div class="user-info">
                <div class="user-pass">
                
                  <form id="fm1" action="/account/login;jsessionid=2DF4474FF68A230CA324392395F4EEE6.tomcat2?from=http://my.csdn.net/my/mycsdn" method="post">

                    <input id="username" name="username" tabindex="1" placeholder="输入用户名/邮箱/手机号" class="user-name" type="text" value=""/>
                    <div class="mobile-auth" style="display:none"><span>该手机已绑定账号，可使用  </span><a href="" id="mloginurl" class="mobile-btn" >手机验证码登录</a></div>
                    <input id="password" name="password" tabindex="2" placeholder="输入密码" class="pass-word" type="password" value="" autocomplete
>>> 
