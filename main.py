from requests_html import HTMLSession
from bs4 import BeautifulSoup


def amazon_scrape():
    while True:
        try:
            name = input('Enter a product name : ').replace(' ','+')
            url = f'https://www.amazon.in/s?k={name}&crid=6VJPE1FS8BVY&sprefix=Head%2Caps%2C215&ref=nb_sb_ss_ts-doa-p_1_4'
            s = HTMLSession()
            r = s.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'})
            r.html.render(sleep=1)

            soup = BeautifulSoup(r.html.html,'html.parser')
            main_divv = soup.find_all('div',{'class':'sg-row'})
            images = []
            names = []
            prices_symbols = []
            prices = []
            ratings = []
            urls = []

            for divv in main_divv:
                all_images = divv.find_all('img',{'class':'s-image'})
                [images.append(img.attrs['src']) for img in all_images if len(images) < 28 and img.attrs['src'] != 'https://images-na.ssl-images-amazon.com/images/G/31/img20/Wireless/MobileInsider/June/10th/420x420_5._CB429051440_QL95_SY80_.jpg']


                all_names = divv.find_all('h2',{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})
                [names.append(name.text)for name in all_names if len(names) < len(main_divv)]

                all_psymbols = divv.find_all('span',{'class':'a-price-symbol'})
                [prices_symbols.append(symbols.text) for symbols in all_psymbols if len(prices_symbols) < 22]


                all_prices = divv.find_all('span',{'class':'a-price-whole'})
                [prices.append(price.text) for price in all_prices if len(prices) < len(main_divv)]

                all_ratings = divv.find_all('span',{'class':'a-icon-alt'})
                [ratings.append(rating.text) for rating in all_ratings if len(ratings) < len(main_divv)]

                all_urls = divv.find_all('a',{'class':'a-link-normal s-no-outline'})
                [urls.append(url.attrs['href']) for url in all_urls if len(urls) < len(main_divv)]


            for z in zip(images,names,prices_symbols,prices,ratings,urls):
                print(f"\nProduct Image : {z[0]}\nProduct Name : {z[1]}\nProduct Price : {z[2]}{z[3]}\nProduct Rating : {z[4]}\n\nProduct Link : {'https://www.amazon.in'+z[5]}\n\n\n")

        except Exception as e:
            print('Check the spelling and try again.')
            print(e)


if __name__ == '__main__':
    amazon_scrape()
