This is a JSON formatted file containing all the countries, their states and provinces and cities in heirarchical order. A sample python code is provided to give an overview on how to use the data.

The basic format is
```
[
	[
		'Country Name',
		[
			[
				'State/Provice 1',
				[
					'City 1',
					'City 2',
					......
				]

			],

			[
				'State/Provice 2',
				[
					'City 1',
					'City 2',
					......
				]

			],

			.....


		],

		....

	]
]

```

The data was accumulated using the free [Geonames](http://geonames.org) API.
I don't know if the data has any errors, please let me know if someone finds anything.
