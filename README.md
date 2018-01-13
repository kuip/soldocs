# soldocs

Generates Markdown documentation from [populus](https://github.com/ethereum/populus) compiled contracts.json.

## Use

```
virtualenv -p python3 env
. env/bin/activate
pip install soldocs
soldocs --input examples/contracts.json --output examples/docs.md
```
