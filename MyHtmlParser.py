import re

from bs4 import BeautifulSoup


class MyHTMLParser():
    def __init__(self,vData):
        self.__Soup=BeautifulSoup(vData,"html5lib")

        self.__solveData()

    def __solveData(self):
        # Z
        for ZNode in self.__Soup.select("span[class='z']"):
            PZnode=ZNode.find_previous_sibling()
            if PZnode is not None:
                if "gr" in PZnode.attrs.get("class"):
                    ZNode.decompose()

        # Pronunciation
        for FayinNode in self.__Soup.select("a[class='fayin']"):
            FayinNode.img.decompose()
            del FayinNode['href']
        for FayinNode in self.__Soup.select("span[class='ei-g']"):
            for Node in FayinNode.select("span[class='z']"):
                Node.decompose()
            for Node in FayinNode.select("a:nth-of-type(2)"):
                Node.decompose()

        # Definition
        DefinitionNo=1
        for DefinitionNode in self.__Soup.select("span[class='n-g']"):
            NewTag=self.__Soup.new_tag("span")
            NewTag.attrs={"style":"display:inline-block","class":"count"}
            NewTag.string=str(DefinitionNo)
            DefinitionNode.insert(0,NewTag)
            DefinitionNo+=1

        # Example
        for ExanpleNode in self.__Soup.select("span[class='x-g']"):
            ExanpleNode.decompose()
            del FayinNode['href']

        # Totally
        for PracpronNode in self.__Soup.select("span[class='pracpron']"):
            PracpronNode.decompose()

        # Help
        for HelpNode in self.__Soup.select("span[class='help']"):
            HelpNode.decompose()

        # Property
        for PropertyNode in self.__Soup.select("span[class='block-g']"):
            PropertyNode.decompose()

        # IDM
        for IDMNode in self.__Soup.select("span[class='ids-g']"):
            IDMNode.decompose()

        # Bank
        for BankNode in self.__Soup.select("span[class='xr-g']"):
            BankNode.decompose()

        # GR
        for GrNode in self.__Soup.select("span[class='gr']"):
            GrNode.decompose()

        # Count
        for CountNode in self.__Soup.select("span[class='z_n']"):
            CountNode.decompose()


        # test=self.__Soup.prettify()
        pass

    def getData(self):
        self.__Soup.head.append(self.__Soup.new_tag(
            "meta",charset="UTF-8"
        ))

        return self.__Soup.prettify()


