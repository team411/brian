To build the plugin:

* Clone the repo into your plugins folder
  * On OS X: `~/Library/Application Support/LightTable/plugins/`
  * On Linux: `~/.config/LightTable/plugins/`
  * On Windows: `%APPDATALOCAL%/LightTable/plugins/`
* Open [brian.cljs](https://github.com/LightTable/LightTable-Brian/blob/master/src/lt/plugins/brian.cljs)
* Connect an nrepl client to the [project.clj](https://github.com/LightTable/LightTable-Brian/blob/master/project.clj)
* Save [brian.cljs](https://github.com/LightTable/LightTable-Brian/blob/master/src/lt/plugins/brian.cljs) or run the command `Editor: Build file or project`. You should see "Compiled plugin to ...brian_compiled.js" in the statusbar
* Run the command `Plugins: Refresh plugin list` to detect the plugin
* Save [brian.behaviors](https://github.com/LightTable/Brian/blob/master/brian.behaviors) or run the command `App: Reload behaviors` to load/reload the plugin behaviors

For interactive development, use the built-in clojurescript eval (ctrl-enter by default) and choose the `Light Table UI` connection.

Note: due to [Issue 1042](https://github.com/LightTable/LightTable/issues/1042) the `App: Reload behaviors` command will not reload the plugin source. To pick up changes either use interactive eval or restart Light Table.

Important files are [plugin.edn](https://github.com/LightTable/LightTable-Brian/blob/master/plugin.edn), which contains metadata about the plugin and also points to the behaviors file.  The behaviors listed in [brian.behaviors](https://github.com/LightTable/LightTable-Brian/blob/master/brian.behaviors) are loaded by the plugin manager. Most plugins will contain at least `{:+ {:app [(:lt.objs.plugins/load-js "brian_compiled.js" true)]}}` in order to load code into Light Table.
