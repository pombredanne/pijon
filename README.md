# pijon
A json migration tool


## tl;dr
```python
Pijon.migrate_file('json_file.json', '/folder/with/migrations')
```


## Prepare a new migration:
add all the migrations script in a given folder.
You can use a custom naming (ex 'migration_000_first.py') and specify the format along the folder
```python
Pijon.migrate_file('json_file.json', '/folder/with/migrations', file_format='migration_\d+_.+')
```

## Run your migrations
you can migrate either a file or a direct input in json format:
```python
Pijon.migrate('{"my": "awesome", "json": null}', '/folder/with/migrations')
Pijon.migrate_file('json_file.json', '/folder/with/migrations')
```

if an output_file is provided, the updated json will be written inside and input file will remain unchanged
```python
Pijon.migrate_file('json_file.json', '/folder/with/migrations', output_file='new_json.json')
```
