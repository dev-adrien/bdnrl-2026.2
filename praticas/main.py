import sqlite3

con = sqlite3.connect("world.db")
cor = con.cursor()

queries = [
'''
	SELECT * FROM city
		WHERE CountryCode = "BRA" AND
		District = 'Ceará';
''',
'''
	SELECT COUNT(*) FROM city
		WHERE CountryCode = "USA"
''',
'''
	SELECT Population, LifeExpectancy FROM country
		WHERE Code = "ARG"
''',
'''
	SELECT Name, LifeExpectancy FROM country
		ORDER BY LifeExpectancy DESC
		LIMIT 1
''',
'''
	SELECT city.Name FROM country
		JOIN city ON city.ID = country.Capital
		WHERE country.Code = "ESP"
''',
'''
	SELECT countrylanguage.Language FROM country
		JOIN countrylanguage ON countrylanguage.CountryCode = country.Code
		WHERE country.region = "Southeast Asia"
''',
'''
	SELECT COUNT(*) FROM country
''',
'''
    SELECT SUM(GNP) FROM country
''',
'''
	SELECT Name FROM country
		ORDER BY GNP DESC
		LIMIT 1
''',
'''
	SELECT
		Name,
		Population / SurfaceArea AS Densidade
	FROM country
	WHERE Continent = 'Asia'
	ORDER BY Densidade DESC
	LIMIT 3
''',
'''
	SELECT Name, SurfaceArea FROM country
		ORDER BY SurfaceArea
		LIMIT 1
'''


]

for query in queries:
	res = con.execute(query)
	for row in res:
		print(row)

con.close()