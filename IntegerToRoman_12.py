class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        miles = int(num / 1000)
        centenas = int((num - miles*1000) / 100)
        decenas = int((num - miles*1000 - centenas*100) / 10)
        unidades = (num - miles*1000 - centenas*100 - decenas*10)


        if 1 <= miles < 4:
            result += (miles * "M")
        else:
            pass
        if centenas == 9:
            result += "CM"
        else:
            if 5 <= centenas < 9:
                if centenas / 5  == 1:
                    result += "D"
                else:
                    resto_centenas = centenas - 5
                    result += ("D" + resto_centenas * "C")
            else:
                if centenas == 4:
                    result += ("CD")
                else:
                    result += ("C" * centenas)


        if decenas == 9:
            result += "XC"
        else:
            if 5 <= decenas < 9:
                if decenas / 5  == 1:
                    result += "L"
                else:
                    resto_decenas = decenas - 5
                    result += ("L" + (resto_decenas * "X"))
            else:
                if decenas == 4:
                    result += ("XL")
                else:
                    result += ("X" * decenas)

        if unidades == 9:
            result += "IX"
        else:
            if 5 <= unidades < 9:
                if unidades / 5  == 1:
                    result += "V"
                else:
                    resto_unidades = unidades - 5
                    result += ("V" + resto_unidades * "I")
            else:
                if unidades == 4:
                    result += ("IV")
                else:
                    result += ("I" * unidades)

        return result