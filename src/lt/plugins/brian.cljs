(ns lt.plugins.brian
  (:require [lt.objs.editor.pool :as pool]
            [lt.objs.editor :as editor]
            [lt.objs.command :as cmd]
            [lt.objs.tabs :as tabs]
            [lt.util.load :as load]
            [lt.object :as object]
            [lt.plugins.watches :as watches])
  (:require-macros [lt.macros :refer [behavior]]))

;; Define cljs binding to 'request' node module
(def request (load/node-module "request"))

(def browser-opened false)

;; Return current line and full code
(defn get-code []
  (let [ed (lt.objs.find/current-ed)]
    { :code (editor/->val ed) :line (get (editor/->cursor ed "start") :line) }))

;; Fetch data and run render callback
;;(defn get-data [url, callback]
;;  (let [code (get-code)]
;;    (request url (fn [e r body] ((callback (str "http://localhost:5000/static/figure.svg?line=" (get code :line) "&code=" (js/encodeURIComponent (get code :code)) )))))))

;; Open browser to render data
(defn render-data [path]
  (if browser-opened
    (close-btds))
  (cmd/exec! :tabset.new)
  (cmd/exec! :tabset.next)
  (cmd/exec! :add-browser-tab path)
  (cmd/exec! :tabset.prev)
  (def browser-opened true))

;; Close browser tabset
(defn close-btds []
  (cmd/exec! :tabset.next)
  (cmd/exec! :tabs.close)
  (cmd/exec! :tabset.close)
  (def browser-opened false))


;; Main method to visualize data
;;(defn brian-visualize []
;;    (cmd/exec! :tabset.new "tabset")
;;    (get-data "http://localhost:5000/static/figure.svg" render-data))

;; Main method to visualize data
(defn brian-visualize []
  (let [code (get-code)]
      (render-data (str "http://localhost:5000/eval?line=" (get code :line) "&code=" (js/encodeURIComponent (get code :code)) ))))

;; Register global LT command
(cmd/command {:command :brian-visualize
              :desc "Brian: visualize data"
              :exec brian-visualize})






