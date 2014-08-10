if(!lt.util.load.provided_QMARK_('lt.plugins.brian')) {
goog.provide('lt.plugins.brian');
goog.require('cljs.core');
goog.require('lt.objs.tabs');
goog.require('lt.objs.editor.pool');
goog.require('lt.objs.command');
goog.require('lt.plugins.watches');
goog.require('lt.util.load');
goog.require('lt.plugins.watches');
goog.require('lt.objs.editor');
goog.require('lt.object');
goog.require('lt.object');
goog.require('lt.util.load');
goog.require('lt.objs.tabs');
goog.require('lt.objs.editor');
goog.require('lt.objs.editor.pool');
goog.require('lt.objs.command');
lt.plugins.brian.request = lt.util.load.node_module.call(null,"request");
lt.plugins.brian.get_code = (function get_code(){var ed = lt.objs.find.current_ed.call(null);return new cljs.core.PersistentArrayMap(null, 2, [new cljs.core.Keyword(null,"code","code",1016963423),lt.objs.editor.__GT_val.call(null,ed),new cljs.core.Keyword(null,"line","line",1017226086),cljs.core.get.call(null,lt.objs.editor.__GT_cursor.call(null,ed,"start"),new cljs.core.Keyword(null,"line","line",1017226086))], null);
});
lt.plugins.brian.get_data = (function get_data(url,callback){var code = lt.plugins.brian.get_code.call(null);return lt.plugins.brian.request.call(null,url,((function (code){
return (function (e,r,body){return callback.call(null,[cljs.core.str("http://77.88.37.102:5000/static/figure.svg?line="),cljs.core.str(cljs.core.get.call(null,code,new cljs.core.Keyword(null,"line","line",1017226086))),cljs.core.str("&code="),cljs.core.str(encodeURIComponent(cljs.core.get.call(null,code,new cljs.core.Keyword(null,"code","code",1016963423))))].join('')).call(null);
});})(code))
);
});
lt.plugins.brian.render_data = (function render_data(path){lt.objs.command.exec_BANG_.call(null,new cljs.core.Keyword(null,"add-browser-tab","add-browser-tab",3663273910),path);
return lt.objs.command.exec_BANG_.call(null,new cljs.core.Keyword(null,"tabset.prev","tabset.prev",1472322118));
});
lt.plugins.brian.brian_visualize = (function brian_visualize(str){lt.objs.command.exec_BANG_.call(null,new cljs.core.Keyword(null,"tabset.new","tabset.new",1444331601),"tabset");
lt.objs.command.exec_BANG_.call(null,new cljs.core.Keyword(null,"tabset.next","tabset.next",1472250630));
return lt.plugins.brian.get_data.call(null,"http://77.88.37.102:5000/static/figure.svg",lt.plugins.brian.render_data);
});
lt.objs.command.command.call(null,new cljs.core.PersistentArrayMap(null, 3, [new cljs.core.Keyword(null,"command","command",1964298941),new cljs.core.Keyword(null,"brian-visualize","brian-visualize",1676687487),new cljs.core.Keyword(null,"desc","desc",1016984067),"Brian: visualize data",new cljs.core.Keyword(null,"exec","exec",1017031683),lt.plugins.brian.brian_visualize], null));
}

//# sourceMappingURL=brian_compiled.js.map