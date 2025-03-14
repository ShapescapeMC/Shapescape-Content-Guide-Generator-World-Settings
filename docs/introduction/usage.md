(usage)=
# Usage

Here are the default settings of the filter. These settings are optional.

```json
{
    "filter": "shapescape_cgg_world_settings",
    "settings": {
        "release_config_path": "../pack/release_config.json",
        "path_relative_to_config_json": true,
        "world_settings_template_path": "data/shapescape_content_guide_generator/templates/world_settings.md"
        
    }
},
```

- `release_config_path: string` - Path to the release_config.json file
- `path_relative_to_config_json: bool` - If the release_config path is relative
- `world_settings_template_path: string` - Path to the world_settings.md file of the content guide generator

```{note}
This filter is an add-on to the Content Guide Generator. To ensure it works properly, make sure you have installed the latest version of the Content Guide Generator with the newest data. If you're unsure, you can simply delete the data folder of the Content Guide Generator and install it again using the -f argument.
```

```{note}
Please make sure that this is run before the content guide generator for it to work!
```

This filter is used to update the content guide section describing the world settings by using the settings set in the release_config.json
