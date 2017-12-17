nation = ['Afghan',
 'Albanian',
 'Algerian',
 'American',
 'Angolan',
 'Argentine',
 'Australian',
 'Austrian',
 'Azerbaijani',
 'Bahamian',
 'Belgian',
 'Bolivian',
 'Bosnian',
 'Brazilian',
 'British',
 'Bulgarian',
 'Burkinabe',
 'Cambodian',
 'Cameroonian',
 'Canadian',
 'Chilean',
 'Chinese',
 'Colombian',
 'Congolese',
 'Costa Rican',
 'Croatian',
 'Cuban',
 'Czech',
 'Danish',
 'Dutch',
 'Ecuadorian',
 'Egyptian',
 'Estonian',
 'Ethiopian',
 'Filipino',
 'Finnish',
 'French',
 'Georgian',
 'German',
 'Ghanaian',
 'Greek',
 'Guatemalan',
 'Guyanese',
 'Haitian',
 'Hungarian',
 'Icelandic',
 'Indian',
 'Indonesian',
 'Iranian',
 'Iraqi',
 'Irish',
 'Israeli',
 'Italian',
 'Ivorian',
 'Japanese',
 'Kazakhstani',
 'Kenyan',
 'Kuwaiti',
 'Kyrgyzstani',
 'Latvian',
 'Lebanese',
 'Lithuanian',
 'Luxembourgish',
 'Macedonian',
 'Malaysian',
 'Malian',
 'Mauritanian',
 'Mexican',
 'Moroccan',
 'Mozambican',
 'Namibian',
 'New Zealander',
 'Nicaraguan',
 'Nigerian',
 'Norwegian',
 'Pakistani',
 'Palestinian',
 'Panamanian',
 'Paraguayan',
 'Peruvian',
 'Polish',
 'Portuguese',
 'Puerto Rican',
 'Romanian',
 'Russian',
 'Rwandan',
 'Saudi Arabian',
 'Senegalese',
 'Serbian',
 'Singaporean',
 'Slovak',
 'Slovenian',
 'South African',
 'Spanish',
 'Sudanese',
 'Swedish',
 'Swiss',
 'Syrian',
 'Taiwanese',
 'Tanzanian',
 'Thai',
 'Tunisian',
 'Turkish',
 'Ugandan',
 'Ukrainian',
 'Uruguayan',
 'Venezuelan',
 'Vietnamese',
 'Zimbabwean',
 "['American']",
 "['Brisitsh']",
 "['Bristish']",
 "['British']",
 "['Canadian']",
 "['Czech']",
 "['Serbian']",
 "['South Korean']",
 "['Tajikistani']",
 "['Unknown']"]

dep = ['2004-04-22',
 'Architecture & Design',
 'Architecture & Design - Image Archive',
 'Drawings',
 'Film',
 'Fluxus Collection',
 'Media and Performance Art',
 'Painting & Sculpture',
 'Photography',
 'Prints & Illustrated Books']

class search():
    tempspace = ''
    tempspace2 = ''
 
    def __init__(self):
        self.dic = {'nation':'','dep':'', 'inyear':0, 'outyear':0}
        
    def ret(self):
        return self.dic

class inSr(search):
    def __init__(self, inputNation, inputDep, inputStart, inputEnd):
        search.__init__(self)
        self.nation = inputNation
        self.dep = inputDep
        self.inyear = inputStart
        self.outyear = inputEnd
        
    def closestCountry(self):
        self.nation = rambo(search.tempspace,nation)
        return rambo(search.tempspace,nation)
        
    def closestDep(self):
        self.dep = rambo(search.tempspace2,dep)
        return rambo(search.tempspace2,dep)
    def setdictionary(self):
        self.dic['nation'] = self.nation
        self.dic['dep'] = self.dep

    def emptyDic1(self):
        return search.tempspace
    def emptyDic2(self):
        return search.tempspace2
    def blank1(self):
        if self.dic['nation'] == ''  or self.dic['nation'] == 0:
            return True
    def blank2(self):
        if self.dic['dep'] == '' or self.dic['dep'] == 0:
            return True
