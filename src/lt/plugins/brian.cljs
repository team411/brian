(ns lt.plugins.brian
  (:require [lt.objs.editor :as editor]
            [lt.objs.editor.pool :as pool]
            [lt.objs.command :as cmd]
            [lt.util.load :as load])
  (:require-macros [lt.macros :refer [behavior]]))

;;(js/eval (str "alert(" "'ololo'" ")"))

(def request (load/node-module "request"))

(defn get-data [url, callback]
  (request url (fn [e r body] ((callback "http://77.88.37.102:5000/static/figure.svg")))))

(defn render-data [path]
  (cmd/exec! :add-browser-tab path)
  (cmd/exec! :tabset.prev))

(defn brian-visualize [str]
  (cmd/exec! :tabset.new "tabset")
  (cmd/exec! :tabset.next)
  (get-data "http://77.88.37.102:5000/static/figure.svg" render-data))


(cmd/command {:command :brian-visualize
              :desc "Brian: visualize data"
              :exec brian-visualize})



