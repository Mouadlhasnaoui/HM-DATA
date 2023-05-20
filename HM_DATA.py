import requests
import json
import pandas as pd
url = 'https://www2.hm.com/fr_fr/homme/en-ce-moment/best-sellers/_jcr_content/main/productlisting.display.json?sort=stock&image-size=small&image=model&offset=36&page-size=160'
search = 'best_seller'
query_string_parameters ={'sort':'stock',
                        'image-size':'small',
                        'image':'model',
                        'offset':'36',
                        'page-size':'160'}
headers = {
'accept': 'application/json, text/javascript, */*; q=0.01',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
'cache-control': 'no-cache',
'cookie': 'searchType=''; akainst=EU1; INGRESSCOOKIE=1684150856.232.549.477325|e7d7d8d55b0de2ea29c698f6d9886acd; hm-france-cart=219ee2f8-d2fa-4973-91b1-2860c0818a2e; OptanonAlertBoxClosed=2023-05-15T11:41:42.084Z; hmid=FDC55226-B011-4DE0-9FA1-969E987D22AD; AMCVS_32B2238B555215F50A4C98A4%40AdobeOrg=1; _ga=GA1.2.1927026860.1684150908; _gcl_au=1.1.406699037.1684150908; optimizelyEndUserId=oeu1684151006111r0.9300220033235016; hm-france-favourites=""; agCookie=b4b49690-054b-4abb-85df-77753a549759; AKA_A2=A; bm_sz=CE8E157E19DB0F2E9F55ECB2DAAE6F02~YAAQX9MRAr3rECeIAQAAsPewMBNZ31HUx+PrJIf9VtfoIXjokso0hO0K7wkC90SqcxQxcCb+2V4D9NfYN+/E8Tl74EQ+zCliaeKCEySJYmA8HvDE51YP7YmMGFy3R3e8Vg67tPEUdJUGD6EtUHqpf1p+rDPPMm7ARFQf8MddmiFp+70AEdzuctZAR1nZ5/MerJ5fWaZHfFtYq5+IOGtiqd6V813bneaixeXJ8lOBPLbOZMOIv6XpUVeKFu7aCBojrnaG5Mk7WNeD620vjCjap94BbV45dmgtaFBdRefwhw==~3486774~4535856; _abck=4BD5D501BCD4B6AECDB8F90240EC0D07~0~YAAQX9MRAh3sECeIAQAAsvywMAm8NzJAvOEzG3x9f0k8poPQG++x8+SBamEL/bYNJ/UlnGJ6nn4cHL5Ao/jmjMgK2SPkH5Aap2j/yHxiXiJN1f/Sq0qEYkFNbsf7UhG4Y59F9cjzD1FY4H6p4QthFgyuRJnPX2y8iUQw+XjXZE2oxD/iEE8g51b0KY8sD4jnn5KRIFlZD5+xwkSxlzZZuiat84AUqo7Kmz7cPpvzSLeIjEuN38mP9G4h7LYSEQYgOLbt6ilOFqi9QpTV8xP2CgnXlXYDWHY85JCdfiPD4gT/wPoRZ2vu32Vc06wgQ1aBxEMdhM+OEh3P/SB07yXjWt2Vg2tenTmfVhXz79A2gk+E5M1Xh57LtjC+TFMLcXpc36bvAY72hA+tGcuU0kwIBgs=~-1~-1~1684447569; ak_bmsc=9080556076D31435566D301E842949E4~000000000000000000000000000000~YAAQX9MRAszsECeIAQAAZgWxMBPOPnqIrd/a2k3+JsuYvpFPhgjBxgy3ma9qHdpQUASeN4g09Uko351z2S/RlQbQmtOqraAN3Kjm22f5Xc5vVbNSWmLvIEEW+17eeyvBxLlKrgvPV2tkkxsJErX2qwUQSMeAmvSLei6DutOeAHjAI3NA6omH3zn3Lc+gPepPt31tBz/xTK/qa7qfT3iS7o4D8cuhL77zsSr6mn+btz+5KjrahnS+5juLYpJn+zpIg04e59bJDO2dou2Vb2rflfjTQXAURx51mhCswjWmUvFaUNYRRXRzF3LVfnl6+WIUgLmQz1EsXJIJ0nmacLx/JSABFWmwCAyEl71oTQtEUtRAB9oVf+NRtLQtfpTw4zvkFYsV1p95FuxrINnTY9LUi8Ng3m4B5cEu1uQkS3lJIVF/A4ipPcdMZIA4PLhJfm5GAW4Zw46Tqmv6ctUcMCkQ+ptpgnUCOZkR6PLCMcMsc2IO2isTnD7lgw==; _gid=GA1.2.272413497.1684444089; _cs_mk_ga=0.23448283133345504_1684446586595; JSESSIONID=D949E4697BDA14ACA7717FE457F5E93BEDA2B18A7013C2F3DE9C9E14A3CA109643B0CEF2C004DE5C598677DE77748A8CE1582E913254F216BCA62C2098566B36.hybris-ecm-web-545ff8fb55-5q4qj; userCookie=##eyJjYXJ0Q291bnQiOjB9##; searchType=TEXT SEARCH; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+18+2023+23%3A01%3A07+GMT%2B0100+(GMT%2B01%3A00)&version=202301.2.0&isIABGlobal=false&hosts=&consentId=fbf0ef31-7ab2-4c79-a16e-bffeb5dbca2e&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _gat_GA_GLOBAL=1; _gat_GA_LOCAL=1; AMCV_32B2238B555215F50A4C98A4%40AdobeOrg=1176715910%7CMCIDTS%7C19496%7CMCMID%7C73070924125461702887315781203732660278%7CMCAID%7CNONE%7CMCOPTOUT-1684454483s%7CNONE%7CvVersion%7C5.4.0; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+18+2023+23%3A01%3A24+GMT%2B0100+(GMT%2B01%3A00)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=fbf0ef31-7ab2-4c79-a16e-bffeb5dbca2e&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _ga_Z1370GPB5L=GS1.2.1684446587.3.1.1684447284.0.0.0; akamref=fr_fr; akavpau_www2_fr_fr=1684447586~id=86eff614e812f63c099aab57106bec80; bm_sv=33AA6AFB6BA145D4172F36F529A1C471~YAAQd7wvF+S9By6IAQAAPNPhMBNdheSCHueK1hpH5uAJk5rWpv5Z+shyvluosgez2STYUw+qr1VHOqp2JWb8af6yz6L8vbQBkJ99n56ALmUj6zUHQfpJblNtkPc+jdvTnOOPwRO1SagTZ9hrYXrbIk9Ot/IhfZlm+wy7dPVGMGYAEvx6htV0WW1Hh+pJXbcM52+3IxsMm5M2cT11TWmN7PYkUZofLqmhNTqwVxn6eSieuxdivenjKxLnZ2IO~1; utag_main=v_id:01881f36af50001c499a53d59a0c0507c002407400bd0$_sn:2$_se:136$_ss:0$_st:1684449088016$c_consent:C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1$vapi_domain:hm.com$ses_id:1684444088246%3Bexp-session$_pn:13%3Bexp-session$ses_id_r:s_5729411603338503.1684444088246%3Bexp-session$segment:dep-test-data%3Bexp-session$prevpage:%2FMEN%2FSEASONALTRENDING%20%3A%20BESTSELLERS%2FBESTSELLERS%20%3A%20VIEWALL%2FVIEW_ALL%2FMen%20%3A%20Seasonaltrending%20%3A%20Bestsellers%20%3A%20Viewall%3Bexp-1684450883617$cart_active:No%3Bexp-session$fld_qv:4%3Bexp-session',
'pragma': 'no-cache',
'referer': 'https://www2.hm.com/fr_fr/homme/catalogue-par-produit/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=36',
'sec-ch-ua': '"Chromium";v="112", "Not_A Brand";v="24", "Opera GX";v="98"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0',
}
res = requests.request("GET" , url , headers=headers, params=query_string_parameters).json()
   #print(res)
products = []
rows = res['products']
for i in range(0, len(rows)):
    product_name = rows[i]['title']
    prices = rows[i]['price'].replace(',','.').strip()
    categories = rows[i]['category']
    links = rows[i]['link']
    products.append(
        (product_name,prices,categories,links)
    )
df = pd.DataFrame(products, columns=['Product Name', 'Product Price', 'Product category', 'Product link'])
print(df)
df.to_excel('HM.xlsx', index=False)
print('data saved ')
