(function(t){function e(e){for(var n,s,r=e[0],c=e[1],l=e[2],d=0,m=[];d<r.length;d++)s=r[d],Object.prototype.hasOwnProperty.call(a,s)&&a[s]&&m.push(a[s][0]),a[s]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(t[n]=c[n]);u&&u(e);while(m.length)m.shift()();return o.push.apply(o,l||[]),i()}function i(){for(var t,e=0;e<o.length;e++){for(var i=o[e],n=!0,r=1;r<i.length;r++){var c=i[r];0!==a[c]&&(n=!1)}n&&(o.splice(e--,1),t=s(s.s=i[0]))}return t}var n={},a={_Demo:0},o=[];function s(e){if(n[e])return n[e].exports;var i=n[e]={i:e,l:!1,exports:{}};return t[e].call(i.exports,i,i.exports,s),i.l=!0,i.exports}s.m=t,s.c=n,s.d=function(t,e,i){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:i})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var i=Object.create(null);if(s.r(i),Object.defineProperty(i,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)s.d(i,n,function(e){return t[e]}.bind(null,n));return i},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],c=r.push.bind(r);r.push=e,r=r.slice();for(var l=0;l<r.length;l++)e(r[l]);var u=c;o.push([0,"chunk-vendors"]),i()})({0:function(t,e,i){t.exports=i("31d3")},"0532":function(t,e,i){"use strict";i.d(e,"a",(function(){return u}));i("4160");var n=i("d4ec"),a=i("bee2"),o=i("c6c6"),s=i.n(o),r={desktop:1920,tablet:768,phone:320},c=1024,l=10,u=function(){function t(){Object(n["a"])(this,t),this.md=new s.a(window.navigator.userAgent),this.$html=document.documentElement,this.$window=window,this.device,this.init()}return Object(a["a"])(t,[{key:"init",value:function(){this.device=this.detectDevice(),this.runScreenResize(),this.bindEvents()}},{key:"detectDevice",value:function(){var t="desktop";return this.md.tablet()?t="tablet":this.md.mobile()&&(t="phone"),document.querySelector(".about-page__text").innerHTML=this.md.os(),document.querySelector(".about-page__text").innerHTML=this._is_touch_device(),t}},{key:"bindEvents",value:function(){var t=this;this.$window.addEventListener("resize",(function(){t.switchBodyClasses(),t.changeBaseFontSize()}))}},{key:"runScreenResize",value:function(){this.switchBodyClasses(),this.changeBaseFontSize()}},{key:"changeBaseFontSize",value:function(){var t=this.calcBaseWidth(),e=this.calculateFontSize(t);this.setPageFontSize(e)}},{key:"calcBaseWidth",value:function(){return r[this.device]}},{key:"calculateFontSize",value:function(t){var e=document.documentElement.clientWidth;e="tablet"===this.device?Math.min(this.$window.innerWidth,t):Math.min(Math.max(this.$window.innerWidth,c),t);var i=e/t*l+"px";return i}},{key:"getTargetWidth",value:function(){return Math.min(this.$window.innerWidth(),r)}},{key:"setPageFontSize",value:function(t){this.$html.style.fontSize=t}},{key:"switchBodyClasses",value:function(){var t=document.body,e=["desktop","tablet","phone"];e.forEach((function(e){return t.classList.remove(e)})),t.classList.add(this.device)}},{key:"_is_touch_device",value:function(){try{return document.createEvent("TouchEvent"),!0}catch(t){return!1}}}]),t}()},"1b35":function(t,e,i){"use strict";var n=i("d576"),a=i.n(n);a.a},"31d3":function(t,e,i){"use strict";i.r(e);var n=i("2b0e"),a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-app",[i("v-content",[i("h1",[t._v("Hello, "),t.user?i("span",{staticClass:"heading1-accent"},[t._v(t._s(t.user.name))]):i("span",{staticClass:"heading1-accent"},[t._v("guest")])]),i("h2",[t._v("Heading 2")]),i("p",[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ")]),i("p",{staticClass:"body-4"},[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ")]),i("p",{staticClass:"body-2"},[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ")]),i("p",{staticClass:"body-1"},[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ")]),i("v-card",{staticClass:"mb-6 pa-6",attrs:{light:""}},[i("v-btn",{attrs:{outlined:""}},[t._v("Logout")])],1),i("div",{staticClass:"mb-10"},[i("div",{staticClass:"mb-6"},[i("v-btn",[t._v("Logout")])],1),i("div",{staticClass:"mb-6"},[i("v-btn",{attrs:{color:"primary"}},[t._v("Add actor")])],1),i("div",{staticClass:"mb-6"},[i("v-btn",{attrs:{large:"",color:"primary"}},[t._v("Search")])],1),i("v-btn",{attrs:{rounded:"","x-large":"",color:"primary"}},[t._v(" Pick a movie for me "),i("v-icon",{staticClass:"ml-5",attrs:{size:"5.6rem"}},[t._v(t._s(t.iconArrowRight))])],1)],1),i("div",[i("div",{staticClass:"mb-6"},[i("v-text-field",{attrs:{label:"First Name","append-icon":t.iconPlus,solo:""},on:{"click:append":t.testInputAppend},model:{value:t.first,callback:function(e){t.first=e},expression:"first"}})],1),i("div",{staticClass:"mb-6"},[i("label",{staticClass:"label"},[t._v("Any genres in mind?")]),i("v-combobox",{attrs:{items:t.items,label:"Select genres from this list","item-color":"white",solo:"",multiple:"",chips:""},scopedSlots:t._u([{key:"selection",fn:function(e){return[i("v-chip",t._b({key:JSON.stringify(e.item),attrs:{color:"primary","input-value":e.selected,disabled:e.disabled},on:{"click:close":function(t){return e.parent.selectItem(e.item)}}},"v-chip",e.attrs,!1),[t._v(" "+t._s(e.item)+" ")])]}}]),model:{value:t.select,callback:function(e){t.select=e},expression:"select"}})],1),i("div",{staticClass:"mb-6"},[i("TimeSlider")],1)]),i("div",{staticClass:"mb-10"},[i("v-dialog",{attrs:{width:"500"},scopedSlots:t._u([{key:"activator",fn:function(e){var n=e.on;return[i("v-btn",t._g({attrs:{color:"primary"}},n),[t._v(" Click Me ")])]}}]),model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[i("v-card",{attrs:{light:""}},[i("div",{staticClass:"pa-6"},[i("v-icon",{staticClass:"dialog-close",attrs:{large:"",color:"black"},on:{click:function(e){t.dialog=!1}}},[t._v(t._s(t.iconClose))]),i("v-card-text",{staticClass:"mt-6"},[t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ")]),i("v-card-actions",{staticClass:"dialog-actions"},[i("div",{staticClass:"mb-4"},[i("v-btn",{attrs:{block:"",color:"primary"},on:{click:function(e){t.dialog=!1}}},[t._v("Manage account ")])],1),i("v-btn",{attrs:{block:"",outlined:""}},[t._v("Logout ")])],1)],1)])],1)],1),i("div",[i("v-avatar",{attrs:{size:"10rem"}},[i("img",{attrs:{src:"https://cdn.vuetifyjs.com/images/john.jpg",alt:"John"}})])],1)],1)],1)},o=[],s=i("94ed"),r=i("7cf4"),c={name:"Demo",data:function(){return{user:window.user,dialog:!1,first:"belfdev@gmail.com",select:["Vuetify","Programming"],items:["Programming","Design","Vue","Vuetify"],iconClose:s["f"],iconPlus:s["n"],iconArrowRight:s["e"]}},methods:{testInputAppend:function(){console.log("testInputAppend")}},components:{TimeSlider:r["a"]}},l=c,u=i("2877"),d=i("6544"),m=i.n(d),v=i("7496"),p=i("8212"),f=i("8336"),b=i("b0af"),h=i("99d9"),g=i("cc20"),y=i("2b5d"),_=i("a75b"),w=i("169a"),k=i("132d"),C=i("8654"),x=Object(u["a"])(l,a,o,!1,null,null,null),S=x.exports;m()(x,{VApp:v["a"],VAvatar:p["a"],VBtn:f["a"],VCard:b["a"],VCardActions:h["a"],VCardText:h["b"],VChip:g["a"],VCombobox:y["a"],VContent:_["a"],VDialog:w["a"],VIcon:k["a"],VTextField:C["a"]});var P=i("b8e3"),j=i("0532");i("8a71");new j["a"],n["a"].config.productionTip=!1,new n["a"]({vuetify:P["a"],render:function(t){return t(S)}}).$mount("#demo")},"7cf4":function(t,e,i){"use strict";var n=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"time-slider"},[i("span",{staticClass:"time-slider__label"},[t._v(t._s(t.timePretty))]),i("div",{staticClass:"time-slider__input"},[i("v-slider",{attrs:{name:t.name,color:"white","thumb-color":"primary",step:"30",min:"30",max:"240",ticks:""},model:{value:t.minutes,callback:function(e){t.minutes=e},expression:"minutes"}})],1)])},a=[],o=(i("99af"),{props:["name"],computed:{timePretty:function(){var t,e=this.minutes;if(e<60)t="".concat(e," minutes");else{var i=e/60,n=i>1?"s":"";t="".concat(i," hour").concat(n)}return t}},data:function(){return{minutes:120}}}),s=o,r=(i("1b35"),i("2877")),c=i("6544"),l=i.n(c),u=i("ba0d"),d=Object(r["a"])(s,n,a,!1,null,null,null);e["a"]=d.exports;l()(d,{VSlider:u["a"]})},"8a71":function(t,e,i){},b8e3:function(t,e,i){"use strict";var n=i("2b0e"),a=i("f309"),o={primary:"#ffbf69",secondary:"#2d3142",red:"#FF6969",green:"#69FF80",grey100:"#fbfbfb",grey200:"#eaeaea",grey300:"#d3d0c5",grey400:"#a8a8a8",grey500:"#a0a0a0",grey700:"#4b4b4b",grey800:"#363636",grey950:"#282828",grey960:"#262626",grey970:"#242424",grey985:"#2b2b2b",grey980:"#191919",grey990:"#151515",bodyText:"#fbfbfb",bodyBg:"#242424"};n["a"].use(a["a"]);var s={theme:{themes:{dark:o},dark:!0,options:{customProperties:!0}},icons:{iconfont:"mdiSvg"}};e["a"]=new a["a"](s)},d576:function(t,e,i){}});