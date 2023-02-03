# graph_util

A playground project for exploring the MS Graph

## Setup

To set up the CLI:

```bash
# If not already signed in with az:
az login

# Install CLI
python setup.py install

# Configure bash completion (add to .bashrc to auto-load in new shell sessions`)
source <(_GRAPHUTIL_COMPLETE=bash_source graphutil)

# Check installed
graphutil --help
```

## Command output

### Output formats

Most commands support formatting output as `table` (default), `json`, `jsonc`, `raw`, or `none` via the `--output` option. This can also be controlled using the `GRAPHUTIL_OUTPUT` environment variable, i.e. set `GRAPHUTIL_OUTPUT` to `table` to default to the table output format.

| Option  | Description                                                                   |
| ------- | ----------------------------------------------------------------------------- |
| `table` | Works well for interactive use                                                |
| `json`  | Plain JSON output, ideal for parsing via `jq` or other tools                  |
| `jsonc` | Coloured, formatted JSON                                                      |
| `raw`   | Results are output as-is. Useful with `--query` when capturing a single value |
| `none`  | No output                                                                     |

### Querying output

Most commands support [JMESPath](https://jmespath.org/) queries for the output via the `--query` option.

For example, to get a list of name of reports for someone@example.com run `graphutil user reports someone@example.com --query [].name`.

This can be combined with `--output table`, e.g. `graphutil user reports someone@example.com -o table --query '[].{name:name, email:email}'`. Note that the query result must be an object with named properties (or an array of such objects)

## Usage

### User

`user` is a command group for user-related commands.

#### reports

To get a list of reports for a user:

```bash
graphutil user reports someone@example.com
```

To get a list of reports for a user in a specific region:

```bash
graphutil user reports someone@example.com --output table --query "[?contains(department, 'EMEA')]"
```

#### photo

To get a photo for a user:

```bash
grahputil user photo someone@example.com output_filename.jpg
```

This can be combined with other queries, e.g.

```bash
graphutil user reports someone@example.com --output json  --query "[?contains(department, 'EMEA')] | [].upn" \
	| jq -r ".[]"\
	| xargs -I {} graphutil user photo {} {}.jpg
```

