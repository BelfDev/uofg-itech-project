(function(t){function e(e){for(var n,i,o=e[0],c=e[1],l=e[2],d=0,v=[];d<o.length;d++)i=o[d],Object.prototype.hasOwnProperty.call(r,i)&&r[i]&&v.push(r[i][0]),r[i]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(t[n]=c[n]);u&&u(e);while(v.length)v.shift()();return s.push.apply(s,l||[]),a()}function a(){for(var t,e=0;e<s.length;e++){for(var a=s[e],n=!0,o=1;o<a.length;o++){var c=a[o];0!==r[c]&&(n=!1)}n&&(s.splice(e--,1),t=i(i.s=a[0]))}return t}var n={},r={History:0},s=[];function i(e){if(n[e])return n[e].exports;var a=n[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,i),a.l=!0,a.exports}i.m=t,i.c=n,i.d=function(t,e,a){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(i.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)i.d(a,n,function(e){return t[e]}.bind(null,n));return a},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],c=o.push.bind(o);o.push=e,o=o.slice();for(var l=0;l<o.length;l++)e(o[l]);var u=c;s.push([6,"chunk-vendors"]),a()})({"0426":function(t,e,a){"use strict";var n=a("2627"),r=a.n(n);r.a},"0532":function(t,e,a){"use strict";a.d(e,"a",(function(){return u}));a("4160");var n=a("d4ec"),r=a("bee2"),s=a("c6c6"),i=a.n(s),o={desktop:1920,tablet:768,phone:320},c=1024,l=10,u=function(){function t(){Object(n["a"])(this,t),this.md=new i.a(window.navigator.userAgent),this.$html=document.documentElement,this.$window=window,this.device,this.init()}return Object(r["a"])(t,[{key:"init",value:function(){this.device=this.detectDevice(),this.runScreenResize(),this.bindEvents()}},{key:"detectDevice",value:function(){var t=this,e="desktop";return this.md.tablet()?e="tablet":this.md.mobile()&&(e="phone"),setTimeout((function(){console.log(t.md.os()),console.log(t.md.userAgent()),console.log(t._is_touch_device()),document.body.innerHTML="OS: "+t.md.os()+"<br />UserAgent: "+t.md.userAgent()+"<br />Is touch: "+ +t._is_touch_device()+"<br />Is mobile: "+t.md.mobile()+"<br />Is tablet: "+t.md.tablet()+"<br />Version: "+t.md.version()+"<br />Is phone: "+t.md.phone()}),5e3),e}},{key:"bindEvents",value:function(){var t=this;this.$window.addEventListener("resize",(function(){t.switchBodyClasses(),t.changeBaseFontSize()}))}},{key:"runScreenResize",value:function(){this.switchBodyClasses(),this.changeBaseFontSize()}},{key:"changeBaseFontSize",value:function(){var t=this.calcBaseWidth(),e=this.calculateFontSize(t);this.setPageFontSize(e)}},{key:"calcBaseWidth",value:function(){return o[this.device]}},{key:"calculateFontSize",value:function(t){var e=document.documentElement.clientWidth;e="tablet"===this.device?Math.min(this.$window.innerWidth,t):Math.min(Math.max(this.$window.innerWidth,c),t);var a=e/t*l+"px";return a}},{key:"getTargetWidth",value:function(){return Math.min(this.$window.innerWidth(),o)}},{key:"setPageFontSize",value:function(t){this.$html.style.fontSize=t}},{key:"switchBodyClasses",value:function(){var t=document.body,e=["desktop","tablet","phone"];e.forEach((function(e){return t.classList.remove(e)})),t.classList.add(this.device)}},{key:"_is_touch_device",value:function(){try{return document.createEvent("TouchEvent"),!0}catch(t){return!1}}}]),t}()},"0d87":function(t,e,a){},1269:function(t,e,a){"use strict";var n,r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("header",{staticClass:"page-header"},[t.logo?a("Logo"):t._e(),a("Navigation",{attrs:{isAboutPage:t.isAboutPage}}),t.user?a("HeaderAuth",{attrs:{user:t.user}}):t._e()],1)},s=[],i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("nav",{staticClass:"header-nav"},[t.isAboutPage?t._e():a("a",{staticClass:"link",attrs:{href:"/about/"}},[t._v("About Us")]),t.isAboutPage?a("a",{staticClass:"link",attrs:{href:"/"}},[t._v("Home")]):t._e()])},o=[],c={name:"Navigation",props:{isAboutPage:Boolean}},l=c,u=a("2877"),d=Object(u["a"])(l,i,o,!1,null,null,null),v=d.exports,m=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{directives:[{name:"closable",rawName:"v-closable",value:{exclude:["button"],handler:"onClose"},expression:"{ exclude: ['button'], handler: 'onClose' }"}],staticClass:"header-auth-wrapper"},[a("v-btn",{ref:"button",staticClass:"header-auth",attrs:{text:"",rounded:""}},[a("v-avatar",{attrs:{size:"10rem"},on:{click:function(e){t.overlay=!t.overlay}}},[t.user.picture?a("img",{attrs:{src:t.user.picture,alt:t.user.name}}):a("div",{staticClass:"header-auth__anonymous"},[a("v-icon",{attrs:{size:"6rem",color:"secondary"}},[t._v(t._s(t.iconUser))])],1)])],1),t.user?a("v-overlay",{attrs:{absolute:!0,color:"",value:t.overlay}},[a("v-card",{attrs:{light:""}},[a("div",{staticClass:"pa-6"},[a("v-icon",{staticClass:"dialog-close",attrs:{large:"",color:"black"},on:{click:function(e){t.overlay=!1}}},[t._v(t._s(t.iconClose)+" ")]),a("v-card-text",{staticClass:"text-center pa-0"},[a("v-avatar",{staticClass:"mb-6",attrs:{size:"13rem"}},[t.user.picture?a("img",{attrs:{src:t.user.picture,alt:t.user.name}}):a("div",{staticClass:"header-auth__anonymous"},[a("v-icon",{attrs:{size:"10rem",color:"secondary"}},[t._v(t._s(t.iconUser))])],1)]),t.user.name?a("h3",[t._v(t._s(t.user.name))]):t._e(),t.user.email?a("p",{staticClass:"body-3 mt-2 mb-8"},[t._v(t._s(t.user.email))]):a("p",{staticClass:"body-3 mt-2 mb-8"},[t._v("Welcome to "),a("strong",[t._v("Pickee!")])]),a("div",{staticClass:"pl-12 pr-12 ml-12 mr-12 pl-p-0 pr-p-0 ml-p-0 mr-p-0"},[t.user.id?[a("v-btn",{staticClass:"mb-4 pl-6 pr-6",attrs:{block:"",color:"primary",href:"/profile/"}},[t._v("Manage account ")]),a("v-btn",{attrs:{block:"",outlined:"",href:"/logout/"}},[t._v("Logout")])]:[a("v-btn",{staticClass:"mb-4",attrs:{block:"",color:"primary",href:"/login/"}},[t._v("Login ")]),a("v-btn",{staticClass:"pl-6 pr-6",attrs:{block:"",outlined:"",href:"/signup/"}},[t._v("Create account")])]],2)],1)],1)])],1):t._e()],1)},f=[],h=(a("4160"),a("159b"),a("2b0e")),p=a("94ed");h["a"].directive("closable",{bind:function(t,e,a){n=function(n){n.stopPropagation();var r=e.value,s=r.handler,i=r.exclude,o=!1;i.forEach((function(t){if(!o){var e=a.context.$refs[t];o=e.$el.contains(n.target)}})),t.contains(n.target)||o||a.context[s]()},document.addEventListener("click",n),document.addEventListener("touchstart",n)},unbind:function(){document.removeEventListener("click",n),document.removeEventListener("touchstart",n)}});var b={name:"HeaderAuth",props:["user"],methods:{onClose:function(){this.overlay=!1}},data:function(){return{overlay:!1,iconUser:p["a"],iconClose:p["f"]}}},_=b,g=(a("604d"),a("6544")),y=a.n(g),w=a("8212"),C=a("8336"),k=a("b0af"),x=a("99d9"),P=a("132d"),E=a("a797"),O=Object(u["a"])(_,m,f,!1,null,null,null),A=O.exports;y()(O,{VAvatar:w["a"],VBtn:C["a"],VCard:k["a"],VCardText:x["b"],VIcon:P["a"],VOverlay:E["a"]});var L=a("e532"),j={name:"PageHeader",props:{logo:Boolean,isAboutPage:Boolean,user:Object},components:{Navigation:v,HeaderAuth:A,Logo:L["a"]}},$=j,z=(a("0426"),Object(u["a"])($,r,s,!1,null,null,null));e["a"]=z.exports},1336:function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[t.drawer?t._e():a("v-btn",{staticClass:"nav-drawer-activator",attrs:{icon:"",color:"white"},on:{click:function(e){t.drawer=!0}}},[a("v-icon",{attrs:{size:"5rem"}},[t._v(t._s(t.iconMenu))])],1),a("v-navigation-drawer",{staticClass:"nav-drawer",attrs:{width:"38rem",fixed:"","mobile-break-point":t.drawer?0:1024},model:{value:t.drawer,callback:function(e){t.drawer=e},expression:"drawer"}},[a("div",{staticClass:"nav-drawer__logo"},[a("Logo")],1),a("NavDrawerLinks",{attrs:{links:t.links}}),a("div",{staticClass:"nav-drawer__logout-btn"},[a("v-btn",{attrs:{block:"",href:"/logout/"}},[t._v("Logout")])],1)],1)],1)},r=[],s=a("e532"),i=a("94ed"),o=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"nav-drawer-links"},[t._l(t.links,(function(e){return[a("a",{key:e.url,staticClass:"nav-drawer-links__item",class:{"nav-drawer-links__item--active":t.isActive(e.url)},attrs:{href:e.url}},[a("v-icon",{staticClass:"mr-3"},[t._v(t._s(e.icon))]),t._v(" "+t._s(e.name)+" ")],1)]}))],2)},c=[],l={name:"NavDrawerLinks",props:["links"],methods:{isActive:function(t){return t===window.location.pathname}},data:function(){return{test:"Test"}}},u=l,d=(a("a538"),a("2877")),v=a("6544"),m=a.n(v),f=a("132d"),h=Object(d["a"])(u,o,c,!1,null,null,null),p=h.exports;m()(h,{VIcon:f["a"]});var b={name:"ProfileNavDrawer",data:function(){return{iconMenu:i["j"],drawer:!!document.body.classList.contains("desktop"),links:[{name:"Profile",url:"/profile/",icon:i["b"]},{name:"Preferences",url:"/preferences/",icon:i["g"]},{name:"History",url:"/history/",icon:i["h"]}]}},components:{Logo:s["a"],NavDrawerLinks:p}},_=b,g=(a("93c6"),a("8336")),y=a("f774"),w=Object(d["a"])(_,n,r,!1,null,null,null);e["a"]=w.exports;m()(w,{VBtn:g["a"],VIcon:f["a"],VNavigationDrawer:y["a"]})},2627:function(t,e,a){},"4a60":function(t,e,a){"use strict";var n=a("be45"),r=a.n(n);r.a},"4cac":function(t,e,a){"use strict";var n=a("0d87"),r=a.n(n);r.a},6:function(t,e,a){t.exports=a("b483")},"604d":function(t,e,a){"use strict";var n=a("ea03"),r=a.n(n);r.a},6474:function(t,e,a){"use strict";var n=a("af06"),r=a.n(n);r.a},"75ad":function(t,e,a){},"8a71":function(t,e,a){},"93c6":function(t,e,a){"use strict";var n=a("f2d8"),r=a.n(n);r.a},a337:function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",{staticClass:"item-list",class:{"item-list--accented":t.accented}},[t._l(t.items,(function(e){return[a("li",{key:e.id,staticClass:"item-list__element"},[a("button",{staticClass:"item-list__element-button",on:{click:function(a){return t.buttonAction(e)}}},[e.image?a("v-avatar",{staticClass:"item-list__element-avatar",attrs:{size:"6.8rem"}},[a("img",{attrs:{src:e.image,alt:e.text}})]):e.picture?a("img",{staticClass:"item-list__element-picture",attrs:{src:e.picture,alt:e.text}}):t._e(),e.logo?a("div",{staticClass:"item-list__element-logo"},[a("img",{attrs:{src:e.logo,alt:e.text}})]):t._e(),a("span",{staticClass:"item-list__element-text"},[t._v(t._s(e.text))]),e.icon?a("v-icon",{staticClass:"item-list__element-icon"},[t._v(t._s(e.icon))]):t._e()],1)])]}))],2)},r=[],s={name:"ItemList",props:{items:Array,buttonAction:Function,accented:Boolean}},i=s,o=(a("4cac"),a("2877")),c=a("6544"),l=a.n(c),u=a("8212"),d=a("132d"),v=Object(o["a"])(i,n,r,!1,null,null,null);e["a"]=v.exports;l()(v,{VAvatar:u["a"],VIcon:d["a"]})},a538:function(t,e,a){"use strict";var n=a("75ad"),r=a.n(n);r.a},af06:function(t,e,a){},b27d:function(t,e,a){},b483:function(t,e,a){"use strict";a.r(e);var n=a("2b0e"),r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-app",[a("div",{staticClass:"profile-page"},[a("ProfileNavDrawer"),a("main",{staticClass:"profile-page-main"},[a("PageHeader"),a("v-content",{staticClass:"profile-page-content"},[a("div",{staticClass:"profile-page-blocks"},[a("ProfileHistoryList",{attrs:{historyItems:t.historyItems}})],1)])],1)],1)])},s=[],i=(a("d81d"),a("b0c0"),a("1269")),o=a("1336"),c=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"history-list-wrapper"},[a("h3",{staticClass:"history-list__header"},[t._v("Recommendation History")]),a("ul",{staticClass:"history-list"},[t._l(t.historyItems,(function(e){return[a("li",{key:e.text,staticClass:"history-list__element"},[e.image?a("v-img",{staticClass:"history-list__element-poster",attrs:{contain:!1,"max-width":"10rem"}},[a("img",{attrs:{src:e.image,alt:e.text}})]):a("div",{staticClass:"history-list__empty-poster"},[a("span",[t._v("Poster not yet available")])]),a("span",{staticClass:"history-list__element-text"},[t._v(t._s(e.text))]),e.icon?a("div",{staticClass:"action-button history-list__element-icon"},[a("v-icon",{attrs:{color:e.color,size:"3.5rem"}},[t._v(t._s(e.icon))])],1):t._e()],1)]}))],2)])},l=[],u=a("a337"),d={name:"ProfileHistoryList",components:{ItemList:u["a"]},props:["historyItems"]},v=d,m=(a("6474"),a("2877")),f=a("6544"),h=a.n(f),p=a("132d"),b=a("adda"),_=Object(m["a"])(v,c,l,!1,null,null,null),g=_.exports;h()(_,{VIcon:p["a"],VImg:b["a"]});var y=a("94ed"),w={REJECTED:{icon:y["o"],color:"red"},ACCEPTED:{icon:y["p"],color:"green"},BOOKMARKED:{icon:y["c"],color:"primary"}},C={name:"History",data:function(){return{historyItems:[]}},components:{PageHeader:i["a"],ProfileNavDrawer:o["a"],ProfileHistoryList:g},beforeMount:function(){var t=document.getElementsByTagName("app")[0],e=t.getAttribute("data");e&&(this.data=JSON.parse(e),this.historyItems=this.data.results.map((function(t){return{image:t.movie.image_url,text:t.movie.name,icon:t.user_choice?w[t.user_choice].icon:null,color:t.user_choice?w[t.user_choice].color:null}})))}},k=C,x=a("7496"),P=a("a75b"),E=Object(m["a"])(k,r,s,!1,null,null,null),O=E.exports;h()(E,{VApp:x["a"],VContent:P["a"]});var A=a("b8e3"),L=a("0532");a("8a71"),a("b27d");new L["a"],n["a"].config.productionTip=!1,new n["a"]({vuetify:A["a"],render:function(t){return t(O)}}).$mount("#history")},b8e3:function(t,e,a){"use strict";var n=a("2b0e"),r=a("f309"),s={primary:"#ffbf69",secondary:"#2d3142",red:"#FF6969",green:"#69FF80",grey100:"#fbfbfb",grey200:"#eaeaea",grey300:"#d3d0c5",grey400:"#a8a8a8",grey500:"#a0a0a0",grey700:"#4b4b4b",grey800:"#363636",grey950:"#282828",grey960:"#262626",grey970:"#242424",grey985:"#2b2b2b",grey980:"#191919",grey990:"#151515",bodyText:"#fbfbfb",bodyBg:"#242424"};n["a"].use(r["a"]);var i={theme:{themes:{dark:s},dark:!0,options:{customProperties:!0}},icons:{iconfont:"mdiSvg"}};e["a"]=new r["a"](i)},be45:function(t,e,a){},e532:function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("a",{staticClass:"logo",attrs:{href:"/"}},[t._v("Pickee")])},r=[],s=(a("4a60"),a("2877")),i={},o=Object(s["a"])(i,n,r,!1,null,null,null);e["a"]=o.exports},ea03:function(t,e,a){},f2d8:function(t,e,a){}});