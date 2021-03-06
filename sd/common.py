#!/usr/bin/python3
# An autogenerated selection of SurpriseDog's common functions relevant to this project.
# To see how this file was created visit: https://github.com/SurpriseDog/Star-Wrangler

def map_nested(func, array):
	"Apply a function to a nested array and return it"
	out = []
	for item in array:
		if type(item) not in (tuple, list):
			out.append(func(item))
		else:
			out.append(map_nested(func, item))
	return out


def undent(text, tab=''):
	"Remove whitespace at the beginning of lines of text"
	return '\n'.join([tab + line.lstrip() for line in text.splitlines()])


def list_get(lis, index, default=''):

	# Fetch a value from a list if it exists, otherwise return default
	# Now accepts negative indexes
	length = len(lis)
	if -length <= index < length:
		return lis[index]
	else:
		return default



'''
&&&&%%%%%&@@@@&&&%%%%##%%%#%%&@@&&&&%%%%%%/%&&%%%%%%%%%%%&&&%%%%%&&&@@@@&%%%%%%%
%%%%%%%%&@&(((((#%%&%%%%%%%%%&@@&&&&&&%%%&&&&&%%%%%%%%%%%&&&&%&%#((((/#@@%%%%%%%
&&%%%%%%&@(*,,,,,,,/%&%%%%%%%&@@&&&&&%%&&&&%%&&%%%%%%%%%%&&&%#*,,,,,,*/&@&%%%%%%
%%%%%%%&@&/*,,,*,*,,*/%&%%%%%&@@&&&&&&%%&&&&&&&%%%%%%&%%%&&%*,,,,,,,,**#@&&%%%%%
&&&&&%%&@#(**********,*(#&%%%&@&&&&%%%%%%%%%&&&%%%%%%&%&&#*****,*******#@&&%%%%%
&&&%%%&&#/***/*****/*,**,*%&%&@@&&&&&&&&&&&&&&&%%%%%%&&#*,,,*/******/***(%&%%%%%
&&&%%%&%/*****///////**,,,,*/%%&&@@@@@@@@@@@@@@@@&&%#*,,,*,*(///////*****#%&%%%%
@@&%%#&#/,,,*/(//((((//**,,*/#&@@@@@&&&&&&&&&&@@@@@%(/*,,**/(/(((/(//*,,*(&&%%%%
&&&%##&#*,,,*////((((/*///(&@&@@&&&#%((//(/###%&@&@@@@#//**//(#(///***,.,/&&%%%%
%%%%%#%#*,,,**////(///((#&&&%@&%%(/*,,......,,/(#%&&&@@@%((/(/#(///**,,,,(&%%%%%
&&%%%#%%/,..***//(#(#%%&@@@&@%(*.,,..       ...,.,/#@&@@@&&%#(((///**,..,#%%%%%%
%&%%%%%#*,****/(##&@@@&@@@@&%*,....           ....,,(&@@@@@@&@&%((//****,(%%%%%%
%&%%%%%#/,**/#&@@@&@@@@@@@&(*,......    .     ..,..,.(&@@@@@@@&@@@&%#**,*(%%%%%%
&&%%%%#&#(#&@@@&@@@@@@@@%((#@@%&&((,,,,,..,,(**(%@@&@%##(&@@@@@@@@&&@@%#(%%%%%%%
&&&%%%%%&&&&&&@@@@@@%###%@(,%&/@@&(%(/*,..,*/%##&&,%@(*&@#((%&@@@@@@&&@&%%%%&&%%
&&%%%%%%&&&@@@@@@@@#((*#@%,#%%&@#%(/**//,****/(#%%%&&%*(@@*/#(&@@@@@@@&&%%%%%%%%
&&&%%%%%&@@@@&%#/,,,,*,(/%&@@&((%(*,*,,*,**,,*,*#%(#@@&%((**,,,,*#(%&@@&&%%%%%%%
&&&%%%%%@@@@%*/*,...,*,,/*#(//#****,***********,**/#/##(/*,*,...,*/*/&@@&%%&%%%%
&&%%%%%%&@@@(//,....,,*/****/,,/**************/***/,,//**/**,....,*//&@@&%%&%%%%
&&&%%%%%&@@%(/*,. ...,****/*/(//*%&@@&%%%%%%&&&&//*/(*/**/**......,/*#&@&%&&&&%%
&&%%%%%%&@@%(**,,....,/**/((/,#&&&&&%#((((((%&&&@&%/*/(/**/*,. ..,,*/((#@&&&&&&%
%&%%%%%%&&#(/**,..,,,***/((,./%&%&&&@&(/#((#@@&&&%&%,,/((*,/*,,..,,,///(%&%&&&&&
&&%%%%%%&#,**,.,..,,*(//(/,,.,&&&@#&@@##%(#&@&%%@&&#.,,/(((//*,,..,,**,*&%&&%&&&
&&%##%%%#/**,,,,..,*/((((*...,,#&##%(#%%&%%###%(%&/,.. **((((/,...,,,,**(%%#%%%&
&&%####(**,,,.,,.,,/(/(//*,,..../%&(##%&&&%%(#%&#, .. .**//(/(*,,..,.,,**/((#%%%
&&&%#///*,........,/(((//**,.   ,,(#%%%%%%&#%##**.   ,,*//((((*,........,*//(%%%
%%%%(/**...       .,/(((///*., .,*(#(%%%%%%%%##/*,..,,*///((/*.      .....**/(%%
%%%%#(,..          .,/((/(//****,/(((###%#%(#///**,,**/((/((*,          .,.,(%%%
&&%%%#/*...          ,*/(/(/((%%&#&#(/%./.*%(#%#%#&&(((/(/*,.          ..,**(&%%
&&%%%%(*.....          ..*((/**(#&&&&&&&%%%&%&&&%(/,*/((*..           .,..*(&&%%
&&%%%%&#*.      .        */(#/*,,*/((%#%%%%%((**,.*/(#(/,       .       ,(%&%%&%
%%%%%%&%#//**,..           .**(((*,...,,**,,..*,/((/*,.          ...,,//(#%%%%%%
%%%&&&%(/*,**,..,,.,..       .,,**//**,*,,,*,////*,,.        .,.,...,,,**//#%&%%
%%%&&%#/*,*,.    ...      ..         ...  ,.. .       .       ...   ..,,*/(#%&%%
&&&&&%(((*.*... . .*,.   .           .*%%#(,.          .    .*,. ..,.,,**/(%#&%%

Generated by https://github.com/SurpriseDog/Star-Wrangler
a Python tool for picking only the required code from source files
written by SurpriseDog at: https://github.com/SurpriseDog
2021-09-26
'''
