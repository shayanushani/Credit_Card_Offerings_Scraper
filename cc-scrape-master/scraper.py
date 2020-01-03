
import time
from datetime import date
from utils import remove_bad_chars


class Scraper:
    def __init__(self, driver):
        self.driver = driver    # instance variable unique to each instance
        today = date.today()
        now = today.strftime("%m/%d/%y")
        self.all_card_offers = [['Scraped on:', now, '', '', '', '', ''], 
                                ['Credit Card Bank Name', 'Credit Card Name', 'Credit Card Image Link', 'Credit Card Details - Body Information', 'Credit Card APY', 'Credit Card Fee', 'Credit Card Apply Link']]


    
    def new_line(self, bank_name):
        self.all_card_offers.append(['', '', '', '', '', '', ''])
        self.all_card_offers.append([bank_name, '', '', '', '', '', ''])
        self.all_card_offers.append(['', '', '', '', '', '', ''])



    def get_citi_offers(self):
        CITI_LINK = 'https://www.citi.com/credit-cards/compare-credit-cards/citi.action?ID=view-all-credit-cards'
        card_image_base_link = 'https://www.citi.com/CRD/images/card_no_reflection/'
        self.driver.get(CITI_LINK)    
        self.driver.implicitly_wait(10)

        cards = self.driver.find_elements_by_css_selector('div.cA-DD-principal-information')

        bank_name = 'Citi Bank'
        self.new_line(bank_name)

        time.sleep(5)

        for card in cards:
            card_name = card.find_element_by_css_selector('h3.cA-DD-cardTitle').text

            ul = card.find_element_by_css_selector('ul.cA-DD-cardDetails')
            details = ul.find_element_by_css_selector('li.cA-DD-cardDetailsDescription').text
            apr = ul.find_element_by_css_selector('li.apr').text
            fee = ul.find_element_by_css_selector('li.annual-fee').text.replace('Fee1', 'Fee')


            apply_link = card.find_element_by_css_selector('div.cA-DD-cardArtCta').find_element_by_css_selector('a').get_attribute('href')
            
            start = apply_link.find('?ID=')
            end = apply_link.find('&cat')
            if start > 0:
                link_piece = apply_link[start + 4 : end]

            credit_card_image_link = card_image_base_link + link_piece + '.jpg'
        
            card_data = [bank_name, remove_bad_chars(card_name), credit_card_image_link, remove_bad_chars(details), remove_bad_chars(apr), remove_bad_chars(fee), apply_link ]
            self.all_card_offers.append(card_data)
            
        

        
    def get_discover_offers(self):
        DISCOVER_LINK = 'https://www.discover.com/credit-cards/'
        card_image_base_link = 'https://www.discover.com'
        bank_name = 'Discover'
        self.driver.get(DISCOVER_LINK)    
        self.driver.implicitly_wait(10)
        self.new_line(bank_name)

        cards = self.driver.find_elements_by_css_selector('div.cards-offer-wrapper')

        for card in cards:
            card_cont = card.find_element_by_css_selector('div.cards-container')

            apply_link = card_cont.find_element_by_css_selector('a').get_attribute('href')
            card_name = card_cont.find_element_by_css_selector('div.card-textAlign').find_element_by_css_selector('p').find_element_by_css_selector('a').text
            

            if card_name == '':
                card_name = card_cont.find_element_by_css_selector('div.card-textAlign').text

            style_tag = card_cont.find_element_by_css_selector('div.cashback-card').get_attribute('style')

            credit_card_image_link = card_image_base_link + style_tag.split('"')[1]


            card_info = card.find_element_by_css_selector('div.cards-information-wrapper').find_elements_by_css_selector('div')
            details = card_info[0].text.replace('\n', ' ') + ' ' + card_info[1].text.replace('\n', ' ')

            apr = card_info[2].text.replace('\n', ' ')
            fee = 'None'
            

            card_data = [bank_name, remove_bad_chars(card_name), credit_card_image_link, remove_bad_chars(details), remove_bad_chars(apr), remove_bad_chars(fee), apply_link ]
            self.all_card_offers.append(card_data)
        



    def get_capital_one_offers(self):
        CAPITAL_ONE_LINK = 'https://www.capitalone.com/credit-cards/compare/'
        card_image_base_link = 'https://www.capitalone.com'
        bank_name = 'Capital One'
        self.new_line(bank_name)

        self.driver.get(CAPITAL_ONE_LINK)    
        self.driver.implicitly_wait(60)
        time.sleep(10)
    
        main = self.driver.find_element_by_css_selector('ul#product-grid')
        cards = main.find_elements_by_css_selector('li')
        
        for card in cards:
            card_name = card.find_element_by_css_selector('div.cardtitle').find_element_by_css_selector('h3').find_element_by_css_selector('a').find_element_by_css_selector('span').text

            
            credit_card_image_link = card.find_element_by_css_selector('figure.cardimage').find_element_by_css_selector('img').get_attribute('src')
            if 'data:image/gif' in credit_card_image_link:
                credit_card_image_link = card_image_base_link + card.find_element_by_css_selector('figure.cardimage').find_element_by_css_selector('img').get_attribute('data-blazy')
            
            
            apply_link = card.find_element_by_css_selector('apply-now-button').find_element_by_css_selector('a').get_attribute('href')
            
            info = card.find_element_by_css_selector('div.cardmeta')
            details = info.find_element_by_css_selector('div.primary').text.replace('\n', ' ')
            apr = info.find_element_by_css_selector('div.apr').text.replace('\n', ' ')
            fee = info.find_element_by_css_selector('div.fee').text.replace('\n', ' ')
            
            
            card_data = [bank_name, remove_bad_chars(card_name), credit_card_image_link, remove_bad_chars(details), remove_bad_chars(apr), remove_bad_chars(fee), apply_link ]
            self.all_card_offers.append(card_data)
            
            

            


    def get_bank_of_america_offers(self):
        BANK_OF_AMERICA_LINK = 'https://www.bankofamerica.com/credit-cards/#filter'
        self.driver.get(BANK_OF_AMERICA_LINK)    
        self.driver.implicitly_wait(60)
        bank_name = 'Bank Of America'
        self.new_line(bank_name)

        cards = self.driver.find_elements_by_css_selector('div.card-info')
        
        link_list = []
        for card in cards:
            left_right = card.find_elements_by_css_selector('div')
            left = left_right[0]

            link = left.find_element_by_css_selector('a').get_attribute('href')
            
            link_list.append(link)
            

        for link in link_list:
            self.driver.get(link)    
            self.driver.implicitly_wait(60)

            card_name = self.driver.find_element_by_css_selector('h1#skip-to-h1').text
            if card_name == '':
                time.sleep(3)
                card_name = self.driver.find_element_by_css_selector('h1#skip-to-h1').text

            
            credit_card_image_link = self.driver.find_element_by_css_selector('img.card-image').get_attribute('src')

            
            apply_link = self.driver.find_element_by_css_selector('a#applyNow_engagement').get_attribute('href')
            
            details = self.driver.find_element_by_css_selector('div.card-content').text.replace('\n', ' ')

            info = self.driver.find_element_by_css_selector('div.row.rates-table-content').find_elements_by_css_selector('div.medium-4.columns.table-cols')
            apr = 'Introductory APR: ' + info[0].text
            apr += ' Standard APR: ' + info[1].text

            fee = 'Annual Fee: ' + info[2].text

            

            card_data = [bank_name, remove_bad_chars(card_name), credit_card_image_link, remove_bad_chars(details), remove_bad_chars(apr), remove_bad_chars(fee), apply_link ]
            
            self.all_card_offers.append(card_data)



    def get_barclays_offers(self):
        BARCLAYS_LINK = 'https://cards.barclaycardus.com/banking/cards/#///'
        self.driver.get(BARCLAYS_LINK)    
        self.driver.implicitly_wait(60)
        bank_name = 'Barclays'
        self.new_line(bank_name)

        cards = self.driver.find_elements_by_css_selector('article.bcus-card-results__list-item-inner')

        info_list = []
        for card in cards:
            credit_card_image_link = card.find_element_by_css_selector('img.bcus-card-results__list-card-image').get_attribute('src')
            apply_link = card.find_element_by_css_selector('a').get_attribute('href')
            
            details = card.find_element_by_css_selector('ul.bcus-card-results__list-highlights').text.replace('\n', ' ')
            info_list.append([credit_card_image_link, apply_link, details])


        for card in info_list:
            self.driver.get(card[1])
            self.driver.implicitly_wait(60)
            apply_link = card[1]
            credit_card_image_link = card[0]
            details = card[2]
            card_name = self.driver.find_element_by_css_selector('h1#bcus-card-details-hero-header').text
            

            main = self.driver.find_element_by_css_selector('div#card-details-rates-fees')
            fee_and_apr = main.find_elements_by_css_selector('div.bcus-two-col-table-container')
            apr = fee_and_apr[0].text.replace('\n', ' ')
            fee = fee_and_apr[1].text.replace('\n', ' ')
            card_data = [bank_name, remove_bad_chars(card_name), credit_card_image_link, remove_bad_chars(details), remove_bad_chars(apr), remove_bad_chars(fee), apply_link ]
            
            self.all_card_offers.append(card_data)



            
        

    def get_chase_offers(self):
        CHASE_LINK = 'https://creditcards.chase.com/rewards-credit-cards'
        self.driver.get(CHASE_LINK)    
        self.driver.implicitly_wait(60)
        bank_name = 'Chase'
        self.new_line(bank_name)
        cards = self.driver.find_elements_by_css_selector('div.card-box')

        for card in cards:
            card_name = card.find_element_by_css_selector('h3').text.split('.')[0]
            credit_card_image_link = card.find_element_by_css_selector('img.card').get_attribute('src')
            
            details = card.find_element_by_css_selector('div.cardmember-offer').find_element_by_css_selector('p').text.replace('\n', ' ')
            
            apr = card.find_element_by_css_selector('div.purchase-apr').text.split('†')[0]
            
            fee = card.find_element_by_css_selector('div.annual-fee').find_element_by_css_selector('p').text.split('†')[0]
            
            apply_link = card.find_element_by_css_selector('div.buttons-card-box').find_element_by_css_selector('a').get_attribute('href')

            card_data = [bank_name, remove_bad_chars(card_name), credit_card_image_link, remove_bad_chars(details), remove_bad_chars(apr), remove_bad_chars(fee), apply_link ]
            
            self.all_card_offers.append(card_data)
        

    def get_wells_fargo_offers(self):
        WELLS_FARGO_LINK = 'https://www.wellsfargo.com/credit-cards/find-a-credit-card/all/'
        self.driver.get(WELLS_FARGO_LINK)    
        self.driver.implicitly_wait(60)
        bank_name = 'Wells Fargo'
        self.new_line(bank_name)

        link_list = []
        cards = self.driver.find_elements_by_css_selector('div.c101.clearfix')
        for card in cards:
            link = card.find_element_by_css_selector('div.btnContainer').find_element_by_css_selector('a').get_attribute('href')
            
            if link not in link_list:
                link_list.append(link)
        
        for link in link_list:
            self.driver.get(link)
            self.driver.implicitly_wait(60)

            apply_link = link
            card_name = self.driver.find_element_by_css_selector('div#title').text
            
            credit_card_image_link = self.driver.find_element_by_css_selector('figure').find_element_by_css_selector('img').get_attribute('src')

            details = self.driver.find_element_by_css_selector('div.c89featureList').text.replace('\n', ' ')
            
            
            cont = self.driver.find_element_by_css_selector('div#feesandrates').text.split('\n')
        
            fee = cont[1] + ' ' + cont[2]
            apr = ''
            for c in cont[4:12]:
                apr += c + ' '
            
            
            card_data = [bank_name, remove_bad_chars(card_name), credit_card_image_link, remove_bad_chars(details), remove_bad_chars(apr), remove_bad_chars(fee), apply_link ]
            
            self.all_card_offers.append(card_data)
            



    def get_us_bank_offers(self):
        US_BANK_LINK = 'https://www.usbank.com/credit-cards.html'
        self.driver.get(US_BANK_LINK)    
        self.driver.implicitly_wait(60)
        bank_name = 'US Bank'
        self.new_line(bank_name)
        cards = self.driver.find_elements_by_css_selector('div.credit-card-block')

        for card in cards:
            credit_card_image_link = card.find_element_by_css_selector('img.largeImgpath').get_attribute('src')
            card_name = card.find_element_by_css_selector('div.card-title').text
        

            fee = card.find_element_by_css_selector('div.annualFee').text.replace('\n', ' ')
            
            info = card.find_element_by_css_selector('div.welcomeOffer').find_elements_by_css_selector('p')
            
            apr = ''
            details = ''
            for piece in info:
                if 'APR' in piece.text:
                    apr = piece.text
                else:
                    details += piece.text + ' '

            if apr == '':
                apr = '<MISSING>'
            
            details += card.find_element_by_css_selector('div.keyBenefits').find_element_by_css_selector('p').text
            details = details.strip()
            apply_link = card.find_element_by_css_selector('a.colorCards').get_attribute('href')
            
            card_data = [bank_name, remove_bad_chars(card_name), credit_card_image_link, remove_bad_chars(details), remove_bad_chars(apr), remove_bad_chars(fee), apply_link ]
            
            self.all_card_offers.append(card_data)

            
    def get_american_express_offers(self):
        AMERICAN_EXPRESS_LINK = 'https://www.americanexpress.com/us/credit-cards/?category=all'
        self.driver.get(AMERICAN_EXPRESS_LINK)    
        self.driver.implicitly_wait(60)
        bank_name = 'American Express'
        self.new_line(bank_name)
        cards = self.driver.find_elements_by_css_selector('div.acqconsumer_cardTile___2jDOo')
        
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        doc_height = self.driver.execute_script('return document.body.scrollHeight')
        step = 0
        
        while True:
            # Scroll down to bottom
            step += 300
            
            self.driver.execute_script('window.scrollTo(0, ' + str(step) + ' );')

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            
            if step > doc_height:
                break
            
        
        info_data = []

        for i, card in enumerate(cards):
            credit_card_image_link = card.find_element_by_css_selector('div').find_element_by_css_selector('a').find_element_by_css_selector('img').get_attribute('src')

            cont = card.text.split('\n')
            card_name = cont[0]
            details = ''
            for i, c in enumerate(cont[1:]):
                if 'ANNUAL FEE' in c:

                    fee = cont[2 + i].replace('¤', '').replace('†', '')
                    if 'Apply Now' in fee:
                        fee = cont[1 + i].replace('¤', '').replace('†', '')
                    break
                
                details += c + ' '
                
        
            apply_link = card.find_element_by_css_selector('div.acqconsumer_applyNowWrapper___23STu').find_element_by_css_selector('a').get_attribute('href')
            

            all_a_tags = card.find_elements_by_css_selector('a')
            apr_link = ''
            for a in all_a_tags:
                if 'Rates and Fees' in a.text:
                    apr_link = a.get_attribute('href')
            
            
            info_data.append([apr_link, credit_card_image_link, card_name, fee, details, apply_link])


        for data in info_data:
            if data[0] != '':

                self.driver.get(data[0])
                self.driver.implicitly_wait(60)
            
                apr_rows = self.driver.find_element_by_css_selector('div.table').find_elements_by_css_selector('div.row')
                apr = ''
                for row in apr_rows[:2]:
                    apr += row.text.replace('\n', ' ') + ' '
                    
                apr = apr.strip()

            else:
                apr = '<MISSING>'

            credit_card_image_link = data[1]
            card_name = data[2]
            fee = data[3]
            details = data[4]
            apply_link = data[5]

            card_data = [bank_name, remove_bad_chars(card_name), credit_card_image_link, remove_bad_chars(details), remove_bad_chars(apr), remove_bad_chars(fee), apply_link ]
            
            self.all_card_offers.append(card_data)





            
            




        


        
    
            
            


        
    
