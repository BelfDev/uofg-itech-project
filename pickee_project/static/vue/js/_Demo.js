(function(t){function e(e){for(var a,r,s=e[0],c=e[1],l=e[2],d=0,m=[];d<s.length;d++)r=s[d],Object.prototype.hasOwnProperty.call(o,r)&&o[r]&&m.push(o[r][0]),o[r]=0;for(a in c)Object.prototype.hasOwnProperty.call(c,a)&&(t[a]=c[a]);u&&u(e);while(m.length)m.shift()();return n.push.apply(n,l||[]),i()}function i(){for(var t,e=0;e<n.length;e++){for(var i=n[e],a=!0,s=1;s<i.length;s++){var c=i[s];0!==o[c]&&(a=!1)}a&&(n.splice(e--,1),t=r(r.s=i[0]))}return t}var a={},o={_Demo:0},n=[];function r(e){if(a[e])return a[e].exports;var i=a[e]={i:e,l:!1,exports:{}};return t[e].call(i.exports,i,i.exports,r),i.l=!0,i.exports}r.m=t,r.c=a,r.d=function(t,e,i){r.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:i})},r.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},r.t=function(t,e){if(1&e&&(t=r(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var i=Object.create(null);if(r.r(i),Object.defineProperty(i,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)r.d(i,a,function(e){return t[e]}.bind(null,a));return i},r.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},r.p="";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],c=s.push.bind(s);s.push=e,s=s.slice();for(var l=0;l<s.length;l++)e(s[l]);var u=c;n.push([0,"chunk-vendors"]),i()})({0:function(t,e,i){t.exports=i("31d3")},"1b35":function(t,e,i){"use strict";var a=i("d576"),o=i.n(a);o.a},"31d3":function(t,e,i){"use strict";i.r(e);var a=i("2b0e"),o=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-app",[i("v-content",[i("h1",[t._v("Feeling "),i("span",{staticClass:"heading1-accent"},[t._v("Pickee?")])]),i("h2",[t._v("Heading 2")]),i("p",[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ")]),i("p",{staticClass:"body-4"},[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ")]),i("p",{staticClass:"body-2"},[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ")]),i("p",{staticClass:"body-1"},[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ")]),i("v-card",{staticClass:"mb-6 pa-6",attrs:{light:""}},[i("v-btn",{attrs:{outlined:""}},[t._v("Logout")])],1),i("div",{staticClass:"mb-10"},[i("div",{staticClass:"mb-6"},[i("v-btn",[t._v("Logout")])],1),i("div",{staticClass:"mb-6"},[i("v-btn",{attrs:{color:"primary"}},[t._v("Add actor")])],1),i("div",{staticClass:"mb-6"},[i("v-btn",{attrs:{large:"",color:"primary"}},[t._v("Search")])],1),i("v-btn",{attrs:{rounded:"","x-large":"",color:"primary"}},[t._v("Pick a movie for me "),i("v-icon",{staticClass:"ml-5",attrs:{size:"56"}},[t._v(t._s(t.iconArrowRight))])],1)],1),i("div",[i("div",{staticClass:"mb-6"},[i("v-text-field",{attrs:{label:"First Name","append-icon":t.iconPlus,solo:""},on:{"click:append":t.testInputAppend},model:{value:t.first,callback:function(e){t.first=e},expression:"first"}})],1),i("div",{staticClass:"mb-6"},[i("label",{staticClass:"label"},[t._v("Any genres in mind?")]),i("v-combobox",{attrs:{items:t.items,label:"Select genres from this list","item-color":"white",solo:"",multiple:"",chips:""},scopedSlots:t._u([{key:"selection",fn:function(e){return[i("v-chip",t._b({key:JSON.stringify(e.item),attrs:{color:"primary","input-value":e.selected,disabled:e.disabled},on:{"click:close":function(t){return e.parent.selectItem(e.item)}}},"v-chip",e.attrs,!1),[t._v(" "+t._s(e.item)+" ")])]}}]),model:{value:t.select,callback:function(e){t.select=e},expression:"select"}})],1),i("div",{staticClass:"mb-6"},[i("TimeSlider")],1)]),i("div",{staticClass:"mb-10"},[i("v-dialog",{attrs:{width:"500"},scopedSlots:t._u([{key:"activator",fn:function(e){var a=e.on;return[i("v-btn",t._g({attrs:{color:"primary"}},a),[t._v(" Click Me ")])]}}]),model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[i("v-card",{attrs:{light:""}},[i("div",{staticClass:"pa-6"},[i("v-icon",{staticClass:"dialog-close",attrs:{large:"",color:"black"},on:{click:function(e){t.dialog=!1}}},[t._v(t._s(t.iconClose))]),i("v-card-text",{staticClass:"mt-6"},[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ")]),i("v-card-actions",{staticClass:"dialog-actions"},[i("div",{staticClass:"mb-4"},[i("v-btn",{attrs:{block:"",color:"primary"},on:{click:function(e){t.dialog=!1}}},[t._v("Manage account ")])],1),i("v-btn",{attrs:{block:"",outlined:""}},[t._v("Logout ")])],1)],1)])],1)],1),i("div",[i("v-avatar",{attrs:{size:"100"}},[i("img",{attrs:{src:"https://cdn.vuetifyjs.com/images/john.jpg",alt:"John"}})])],1)],1)],1)},n=[],r=i("94ed"),s=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"time-slider"},[i("span",{staticClass:"time-slider__label"},[t._v(t._s(t.timePretty))]),i("div",{staticClass:"time-slider__input"},[i("v-slider",{attrs:{color:"white","thumb-color":"primary",step:"30",min:"30",max:"240",ticks:""},model:{value:t.minutes,callback:function(e){t.minutes=e},expression:"minutes"}})],1)])},c=[],l=(i("99af"),{computed:{timePretty:function(){var t,e=this.minutes;if(e<60)t="".concat(e," minutes");else{var i=e/60,a=i>1?"s":"";t="".concat(i," hour").concat(a)}return t}},data:function(){return{minutes:30}}}),u=l,d=(i("1b35"),i("2877")),m=i("6544"),p=i.n(m),v=i("ba0d"),b=Object(d["a"])(u,s,c,!1,null,null,null),f=b.exports;p()(b,{VSlider:v["a"]});var g={name:"Demo",data:function(){return{dialog:!1,first:"belfdev@gmail.com",select:["Vuetify","Programming"],items:["Programming","Design","Vue","Vuetify"],iconClose:r["b"],iconPlus:r["c"],iconArrowRight:r["a"]}},methods:{testInputAppend:function(){console.log("testInputAppend")}},components:{TimeSlider:f}},y=g,_=(i("4ddb"),i("7496")),h=i("8212"),C=i("8336"),k=i("b0af"),x=i("99d9"),w=i("cc20"),P=i("2b5d"),V=i("a75b"),j=i("169a"),O=i("132d"),S=i("8654"),A=Object(d["a"])(y,o,n,!1,null,null,null),q=A.exports;p()(A,{VApp:_["a"],VAvatar:h["a"],VBtn:C["a"],VCard:k["a"],VCardActions:x["a"],VCardText:x["b"],VChip:w["a"],VCombobox:P["a"],VContent:V["a"],VDialog:j["a"],VIcon:O["a"],VTextField:S["a"]});var L=i("b8e3");i("8a71");a["a"].config.productionTip=!1,new a["a"]({vuetify:L["a"],render:function(t){return t(q)}}).$mount("#demo")},"4ddb":function(t,e,i){"use strict";var a=i("55c6"),o=i.n(a);o.a},"55c6":function(t,e,i){},"8a71":function(t,e,i){},b8e3:function(t,e,i){"use strict";var a=i("2b0e"),o=i("f309"),n={primary:"#ffbf69",secondary:"#2d3142",grey100:"#fbfbfb",grey200:"#eaeaea",grey300:"#d3d0c5",grey400:"#a8a8a8",grey500:"#a0a0a0",grey700:"#4b4b4b",grey800:"#363636",grey950:"#282828",grey960:"#262626",grey970:"#242424",grey980:"#191919",grey990:"#151515",bodyText:"#fbfbfb",bodyBg:"#242424"};a["a"].use(o["a"]);var r={theme:{themes:{dark:n},dark:!0,options:{customProperties:!0}},icons:{iconfont:"mdiSvg"}};e["a"]=new o["a"](r)},d576:function(t,e,i){}});