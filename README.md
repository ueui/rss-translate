# rss-translate

rss translate any to any

![](https://github.com/ueui/rss-translate/workflows/circle_translate/badge.svg)
![](https://github.com/ueui/rss-translate/workflows/Deploy/badge.svg)

you can edit [test.ini](https://github.com/ueui/rss-translate/edit/main/test.ini) to add orginal rss url. [help](https://github.com/ueui/rss/issues/2)

next find the translated link in [https://talengu.github.io/rss-translate/](https://talengu.github.io/rss-translate/)

## 20230814 update
- support proxy mode. you can set `action = "proxy"` in test.ini like [source010](https://github.com/ueui/rss-translate/blob/f6648c5262f4fa0926310dbe43fff820bf727ac7/test.ini#L67).
 Proxy mode does not translate the rss, and directly show the original rss.

## 20230702 update 
- use [main2.py](https://github.com/ueui/rss-translate/blob/main/main2.py) in [circle_translate.yml](https://github.com/ueui/rss-translate/blob/aeb61bc36eb1a22fd003677b5209291cf7cb4a87/.github/workflows/circle_translate.yml#L38)
- atom is bad now base on an atom paraser to find. NOW SUPPORT
        use [feedparser](https://pythonhosted.org/feedparser/)
- fix google translate limit . NOW SUPPORT

## rss translate links

 - source001 [https://politepol.com/fd/reoQ2EA9MDxJ.xml](https://politepol.com/fd/reoQ2EA9MDxJ.xml) -> [bloomberg_news](rss/bloomberg_news)
 - source002 [https://feeds.bloomberg.com/Crypto/news.rss](https://feeds.bloomberg.com/Crypto/news.rss) -> [Bloomberg_Crypto](rss/Bloomberg_Crypto)
 - source003 [https://www.vice.com/en/rss?locale=en_us](https://www.vice.com/en/rss?locale=en_us) -> [English_VICE](rss/English_VICE)
 - source004 [https://kill-the-newsletter.com/feeds/h541vjjth6mkic38ik3f.xml](https://kill-the-newsletter.com/feeds/h541vjjth6mkic38ik3f.xml) -> [Bloomberg](rss/Bloomberg)
 - source005 [https://siftrss.com/f/WYvvrkAkgX](https://siftrss.com/f/WYvvrkAkgX) -> [特集_日経クロストレンド](rss/%E7%89%B9%E9%9B%86_%E6%97%A5%E7%B5%8C%E3%82%AF%E3%83%AD%E3%82%B9%E3%83%88%E3%83%AC%E3%83%B3%E3%83%89)
 - source006 [https://fetchrss.com/rss/620d11a970b7d1781324262266e2f73edf2f98627b0e7aa2.xml](https://fetchrss.com/rss/620d11a970b7d1781324262266e2f73edf2f98627b0e7aa2.xml) -> [Research_Commentary_Brookings](rss/Research_Commentary_Brookings)
 - source007 [http://fetchrss.com/rss/620d11a970b7d1781324262267d7ba1d141b09f2900edc32.xml](http://fetchrss.com/rss/620d11a970b7d1781324262267d7ba1d141b09f2900edc32.xml) -> [Commentary_and_Articles_RAND](rss/Commentary_and_Articles_RAND)
 - source008 [https://politepol.com/fd/gSkM6dQ8BdqG.xml](https://politepol.com/fd/gSkM6dQ8BdqG.xml) -> [Culture_The_Economist](rss/Culture_The_Economist)
 - source009 [https://kill-the-newsletter.com/feeds/kxnraollt2n0gd03szin.xml](https://kill-the-newsletter.com/feeds/kxnraollt2n0gd03szin.xml) -> [Carnegieendowment](rss/Carnegieendowment)
 - source010 [https://politepol.com/fd/LES08YuDyITn.xml](https://politepol.com/fd/LES08YuDyITn.xml) -> [Culture_GQ](rss/Culture_GQ)
 - source011 [https://politepol.com/fd/k2KTqKohLdMD.xml](https://politepol.com/fd/k2KTqKohLdMD.xml) -> [Pew_Research_Center](rss/Pew_Research_Center)
 - source012 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/spotlight/on-politics/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/spotlight/on-politics/rss.xml) -> [NYT_U.S._Politics](rss/NYT_U.S._Politics)
 - source013 [https://politepol.com/fd/6UsKHJLrGfgp.xml](https://politepol.com/fd/6UsKHJLrGfgp.xml) -> [Briefing The Economist](rss/Briefing%20The%20Economist)
 - source014 [https://fetchrss.com/rss/6518f1be2d18ae56d5360f7265d35fc7c43c5356173e4013.xml](https://fetchrss.com/rss/6518f1be2d18ae56d5360f7265d35fc7c43c5356173e4013.xml) -> [Ideas_Morgan_Stanley](rss/Ideas_Morgan_Stanley)
 - source015 [https://www.bloomberg.com/authors/ARbTQlRLRjE/matthew-s-levine.rss](https://www.bloomberg.com/authors/ARbTQlRLRjE/matthew-s-levine.rss) -> [Matt_Levine_Bloomberg_Opinion_Columnist](rss/Matt_Levine_Bloomberg_Opinion_Columnist)
 - source016 [http://fetchrss.com/rss/620d11a970b7d1781324262267d7bb44b787a0de3a0025c2.xml](http://fetchrss.com/rss/620d11a970b7d1781324262267d7bb44b787a0de3a0025c2.xml) -> [SpecialReportsfromReutersjournalistsaroundtheworld](rss/SpecialReportsfromReutersjournalistsaroundtheworld)
 - source017 [https://politepol.com/fd/Ph2CzpZCj4KE.xml](https://politepol.com/fd/Ph2CzpZCj4KE.xml) -> [a16z news content](rss/a16z%20news%20content)
 - source018 [https://forbes.com/sites/billhardekopf/feed](https://forbes.com/sites/billhardekopf/feed) -> [Bill_Hardekopf](rss/Bill_Hardekopf)
 - source019 [https://politepol.com/fd/C8JCiAISyeUs.xml](https://politepol.com/fd/C8JCiAISyeUs.xml) -> [Forbes_Daily](rss/Forbes_Daily)
 - source020 [https://fetchrss.com/rss/61c328520dbe482d810dbec2667c93bbba9f15b9a309f962.xml](https://fetchrss.com/rss/61c328520dbe482d810dbec2667c93bbba9f15b9a309f962.xml) -> [Goings_On_The_New_Yorker](rss/Goings_On_The_New_Yorker)
 - source021 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/series/us-morning-briefing/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/series/us-morning-briefing/rss.xml) -> [NYT_The_Morning_Newsletter](rss/NYT_The_Morning_Newsletter)
 - source022 [https://politepol.com/fd/QqZjRiPuGPVX.xml](https://politepol.com/fd/QqZjRiPuGPVX.xml) -> [The Marbella Property and Lifestyle Blog](rss/The%20Marbella%20Property%20and%20Lifestyle%20Blog)
 - source023 [https://news.google.com/rss/search?hl=ja&gl=JP&ceid=JP:ja&q=ママ活](https://news.google.com/rss/search?hl=ja&gl=JP&ceid=JP:ja&q=ママ活) -> [Google_ニュース_ママ活](rss/Google_%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9_%E3%83%9E%E3%83%9E%E6%B4%BB)
 - source024 [https://politepol.com/fd/cvqP0wDPuxlB.xml](https://politepol.com/fd/cvqP0wDPuxlB.xml) -> [U.S.Environmental_ProtectionAgency_Perspectives](rss/U.S.Environmental_ProtectionAgency_Perspectives)
 - source025 [http://fetchrss.com/rss/5fd1017a86229a5e2b65bb5267d7bed2297e1745eb088902.xml](http://fetchrss.com/rss/5fd1017a86229a5e2b65bb5267d7bed2297e1745eb088902.xml) -> [Henley_&_Partners_Press_Media_Articles](rss/Henley_%26_Partners_Press_Media_Articles)
 - source026 [https://politepol.com/fd/A4Zkx42Ty32F.xml](https://politepol.com/fd/A4Zkx42Ty32F.xml) -> [Henley_&_Partners_Press_Releases](rss/Henley_%26_Partners_Press_Releases)
 - source027 [https://politepol.com/fd/NNLIg5PEAJ5L.xml](https://politepol.com/fd/NNLIg5PEAJ5L.xml) -> [Science technology The Economist](rss/Science%20technology%20The%20Economist)
 - source028 [https://www.sciencedaily.com/rss/top.xml](https://www.sciencedaily.com/rss/top.xml) -> [sciencedaily top](rss/sciencedaily%20top)
 - source029 [https://hnrss.org/newest?count=50&points=100](https://hnrss.org/newest?count=50&points=100) -> [Hacker News Newest](rss/Hacker%20News%20Newest)
 - source030 [https://politepol.com/fd/DX6BTsW4AqS0.xml](https://politepol.com/fd/DX6BTsW4AqS0.xml) -> [Harvard Law Review](rss/Harvard%20Law%20Review)
 - source031 [https://politepol.com/fd/rlte50rk8Git.xml](https://politepol.com/fd/rlte50rk8Git.xml) -> [事件の最新ニュース記事一覧_週刊女性PRIME](rss/%E4%BA%8B%E4%BB%B6%E3%81%AE%E6%9C%80%E6%96%B0%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7_%E9%80%B1%E5%88%8A%E5%A5%B3%E6%80%A7PRIME)
 - source032 [https://politepol.com/fd/SCOYRPwFGqB4.xml](https://politepol.com/fd/SCOYRPwFGqB4.xml) -> [炎上の最新ニュース記事一覧_週刊女性PRIME](rss/%E7%82%8E%E4%B8%8A%E3%81%AE%E6%9C%80%E6%96%B0%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7_%E9%80%B1%E5%88%8A%E5%A5%B3%E6%80%A7PRIME)
 - source033 [https://gnn.gamer.com.tw/rss.xml](https://gnn.gamer.com.tw/rss.xml) -> [巴哈姆特_GNN_新聞網](rss/%E5%B7%B4%E5%93%88%E5%A7%86%E7%89%B9_GNN_%E6%96%B0%E8%81%9E%E7%B6%B2)
 - source034 [https://politepol.com/fd/NjxHZtldG2if.xml](https://politepol.com/fd/NjxHZtldG2if.xml) -> [Lifeboat News The Blog Safeguarding Humanity](rss/Lifeboat%20News%20The%20Blog%20Safeguarding%20Humanity)
 - source035 [http://fetchrss.com/rss/6091364872635734406c61f268281e0204e3b76427070163.xml](http://fetchrss.com/rss/6091364872635734406c61f268281e0204e3b76427070163.xml) -> [Intelligence Lab Knight Frank](rss/Intelligence%20Lab%20Knight%20Frank)
 - source036 [https://politepol.com/fd/OrUMJqDSzBbh.xml](https://politepol.com/fd/OrUMJqDSzBbh.xml) -> [Y Combinator Email Campaign Archive](rss/Y%20Combinator%20Email%20Campaign%20Archive)
 - source037 [http://fetchrss.com/rss/61c328520dbe482d810dbec267d7c1225734b0a49b069a32.xml](http://fetchrss.com/rss/61c328520dbe482d810dbec267d7c1225734b0a49b069a32.xml) -> [メディア掲載情報_ニホンモニター株式会社](rss/%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E6%8E%B2%E8%BC%89%E6%83%85%E5%A0%B1_%E3%83%8B%E3%83%9B%E3%83%B3%E3%83%A2%E3%83%8B%E3%82%BF%E3%83%BC%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE)
 - source038 [http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d824a7dffb2fb8b6075d63.xml](http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d824a7dffb2fb8b6075d63.xml) -> [US Supreme Court](rss/US%20Supreme%20Court)
 - source039 [https://ftr.fivefilters.net/makefulltextfeed.php?step=3&fulltext=1&url=https://politepol.com/fd/SZI6njI9Qa3c.xml&max=3&links=preserve&exc=&submit=Create+Feed](https://ftr.fivefilters.net/makefulltextfeed.php?step=3&fulltext=1&url=https://politepol.com/fd/SZI6njI9Qa3c.xml&max=3&links=preserve&exc=&submit=Create+Feed) -> [NATURE BRIEFING](rss/NATURE%20BRIEFING)
 - source040 [http://fetchrss.com/rss/6091364872635734406c61f267ea8e8a478137c6c108af72.xml](http://fetchrss.com/rss/6091364872635734406c61f267ea8e8a478137c6c108af72.xml) -> [パパ活_検索結果_日刊SPA!](rss/%E3%83%91%E3%83%91%E6%B4%BB_%E6%A4%9C%E7%B4%A2%E7%B5%90%E6%9E%9C_%E6%97%A5%E5%88%8ASPA%21)
 - source041 [https://politepol.com/fd/72TxPeJk9t5i.xml](https://politepol.com/fd/72TxPeJk9t5i.xml) -> [Tall Urban News CTBUH](rss/Tall%20Urban%20News%20CTBUH)
 - source042 [https://politepol.com/fd/fnaVVKc48n2j.xml](https://politepol.com/fd/fnaVVKc48n2j.xml) -> [US Supreme Court BBC News](rss/US%20Supreme%20Court%20BBC%20News)
 - source043 [https://muddywatersresearch.com/feed/?post_type=reports](https://muddywatersresearch.com/feed/?post_type=reports) -> [Muddy Waters Research](rss/Muddy%20Waters%20Research)
 - source044 [https://mastodon.social/@lawrencelry.rss](https://mastodon.social/@lawrencelry.rss) -> [mastodon_lawrencelry](rss/mastodon_lawrencelry)
 - source045 [https://www.usgs.gov/news/national-news-release/feed](https://www.usgs.gov/news/national-news-release/feed) -> [National News Releases US Geological Survey](rss/National%20News%20Releases%20US%20Geological%20Survey)
 - source046 [https://www.smithsonianmag.com/rss/smart-news/](https://www.smithsonianmag.com/rss/smart-news/) -> [Smithsonianmag Smart News](rss/Smithsonianmag%20Smart%20News)
 - source047 [https://politepol.com/fd/8Tigf8zNTwwv.xml](https://politepol.com/fd/8Tigf8zNTwwv.xml) -> [Intelligence Lab Publication Library Knight Frank](rss/Intelligence%20Lab%20Publication%20Library%20Knight%20Frank)
 - source048 [https://politepol.com/fd/981P7slL9Twv.xml](https://politepol.com/fd/981P7slL9Twv.xml) -> [The Wealth Report Knight Frank](rss/The%20Wealth%20Report%20Knight%20Frank)
 - source049 [https://siftrss.com/f/LbvpaQbPYJQ](https://siftrss.com/f/LbvpaQbPYJQ) -> [Celebrity Legal & Lawsuits](rss/Celebrity%20Legal%20%26%20Lawsuits)
 - source050 [https://politepol.com/fd/yVmdKUpodvQk.xml](https://politepol.com/fd/yVmdKUpodvQk.xml) -> [Games Free For a Limited Time Indie Game Bundles](rss/Games%20Free%20For%20a%20Limited%20Time%20Indie%20Game%20Bundles)
 - source051 [https://www.tandfonline.com/feed/rss/mijp20](https://www.tandfonline.com/feed/rss/mijp20) -> [International Journal of Political Economy](rss/International%20Journal%20of%20Political%20Economy)
 - source052 [https://content.apa.org/journals/apl.rss](https://content.apa.org/journals/apl.rss) -> [Journal of Applied Psychology](rss/Journal%20of%20Applied%20Psychology)
 - source053 [https://www.tandfonline.com/feed/rss/vjrl20](https://www.tandfonline.com/feed/rss/vjrl20) -> [The Journal of Psychology](rss/The%20Journal%20of%20Psychology)
 - source054 [https://onlinelibrary.wiley.com/feed/15405907/most-recent](https://onlinelibrary.wiley.com/feed/15405907/most-recent) -> [American Journal of Political Science](rss/American%20Journal%20of%20Political%20Science)
 - source055 [https://www.tandfonline.com/feed/rss/rics20](https://www.tandfonline.com/feed/rss/rics20) -> [Information Communication Society](rss/Information%20Communication%20Society)
 - source056 [https://www.tandfonline.com/feed/rss/rprn20](https://www.tandfonline.com/feed/rss/rprn20) -> [Porn Studies](rss/Porn%20Studies)
 - source057 [https://politepol.com/fd/PqSPOcclzogO.xml](https://politepol.com/fd/PqSPOcclzogO.xml) -> [Tech News Fortune](rss/Tech%20News%20Fortune)
 - source058 [https://gamerpower.com/rss/games ](https://gamerpower.com/rss/games ) -> [GamerPower Giveaways](rss/GamerPower%20Giveaways)
