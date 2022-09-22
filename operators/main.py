# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

mainLanguageSpain = "Castilian Spanish"
mainLanguageSwitzerland = "Swiss"
print(mainLanguageSpain == mainLanguageSwitzerland)

religionSpain = "Roman Catholic"
religionSwitzerland = "Roman Catholic"
print(religionSpain == religionSwitzerland)

capitalLenghtSpain = len("Madrid")
capitalLenghtSwitzerland = len("Bern")
print(capitalLenghtSpain != capitalLenghtSwitzerland)

gdpSwitzerland = 590.71
gdpSpain = 1714.86
print(gdpSwitzerland > gdpSpain)

popGrowthSpain = 0.13
popGrowthSwitzerland = 0.65
print(popGrowthSpain < 1 and popGrowthSwitzerland < 1)

populationSpain = 47163418
populationSwitzerland = 8508698
TenMil = 10000000
print(populationSpain > 10000000 or populationSwitzerland > 10000000)
print(populationSpain > TenMil or populationSwitzerland >
      TenMil and populationSpain < TenMil or populationSwitzerland < TenMil)
