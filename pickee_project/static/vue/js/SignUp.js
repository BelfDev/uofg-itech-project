(function(e){function t(t){for(var a,s,i=t[0],l=t[1],c=t[2],d=0,v=[];d<i.length;d++)s=i[d],Object.prototype.hasOwnProperty.call(r,s)&&r[s]&&v.push(r[s][0]),r[s]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(e[a]=l[a]);u&&u(t);while(v.length)v.shift()();return o.push.apply(o,c||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],a=!0,i=1;i<n.length;i++){var l=n[i];0!==r[l]&&(a=!1)}a&&(o.splice(t--,1),e=s(s.s=n[0]))}return e}var a={},r={SignUp:0},o=[];function s(t){if(a[t])return a[t].exports;var n=a[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.m=e,s.c=a,s.d=function(e,t,n){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)s.d(n,a,function(t){return e[t]}.bind(null,a));return n},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=t,i=i.slice();for(var c=0;c<i.length;c++)t(i[c]);var u=l;o.push([3,"chunk-vendors"]),n()})({"0426":function(e,t,n){"use strict";var a=n("2627"),r=n.n(a);r.a},"0532":function(e,t,n){"use strict";n.d(t,"a",(function(){return u}));n("4160");var a=n("d4ec"),r=n("bee2"),o=n("c6c6"),s=n.n(o),i={desktop:1920,tablet:768,phone:320},l=1024,c=10,u=function(){function e(){Object(a["a"])(this,e),this.md=new s.a(window.navigator.userAgent),this.$html=document.documentElement,this.$window=window,this.device,this.init()}return Object(r["a"])(e,[{key:"init",value:function(){this.device=this.detectDevice(),this.runScreenResize(),this.bindEvents()}},{key:"detectDevice",value:function(){var e=this,t="desktop";return this.md.tablet()?t="tablet":this.md.mobile()&&(t="phone"),setTimeout((function(){console.log(e.md.os()),console.log(e.md.userAgent()),console.log(e._is_touch_device()),document.body.innerHTML="OS: "+e.md.os()+"<br />UserAgent: "+e.md.userAgent()+"<br />Is touch: "+ +e._is_touch_device()+"<br />Is mobile: "+e.md.mobile()+"<br />Is tablet: "+e.md.tablet()+"<br />Version: "+e.md.version()+"<br />Is phone: "+e.md.phone()}),5e3),t}},{key:"bindEvents",value:function(){var e=this;this.$window.addEventListener("resize",(function(){e.switchBodyClasses(),e.changeBaseFontSize()}))}},{key:"runScreenResize",value:function(){this.switchBodyClasses(),this.changeBaseFontSize()}},{key:"changeBaseFontSize",value:function(){var e=this.calcBaseWidth(),t=this.calculateFontSize(e);this.setPageFontSize(t)}},{key:"calcBaseWidth",value:function(){return i[this.device]}},{key:"calculateFontSize",value:function(e){var t=document.documentElement.clientWidth;t="tablet"===this.device?Math.min(this.$window.innerWidth,e):Math.min(Math.max(this.$window.innerWidth,l),e);var n=t/e*c+"px";return n}},{key:"getTargetWidth",value:function(){return Math.min(this.$window.innerWidth(),i)}},{key:"setPageFontSize",value:function(e){this.$html.style.fontSize=e}},{key:"switchBodyClasses",value:function(){var e=document.body,t=["desktop","tablet","phone"];t.forEach((function(t){return e.classList.remove(t)})),e.classList.add(this.device)}},{key:"_is_touch_device",value:function(){try{return document.createEvent("TouchEvent"),!0}catch(e){return!1}}}]),e}()},1269:function(e,t,n){"use strict";var a,r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("header",{staticClass:"page-header"},[e.logo?n("Logo"):e._e(),n("Navigation",{attrs:{isAboutPage:e.isAboutPage}}),e.user?n("HeaderAuth",{attrs:{user:e.user}}):e._e()],1)},o=[],s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("nav",{staticClass:"header-nav"},[e.isAboutPage?e._e():n("a",{staticClass:"link",attrs:{href:"/about/"}},[e._v("About Us")]),e.isAboutPage?n("a",{staticClass:"link",attrs:{href:"/"}},[e._v("Home")]):e._e()])},i=[],l={name:"Navigation",props:{isAboutPage:Boolean}},c=l,u=n("2877"),d=Object(u["a"])(c,s,i,!1,null,null,null),v=d.exports,h=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{directives:[{name:"closable",rawName:"v-closable",value:{exclude:["button"],handler:"onClose"},expression:"{ exclude: ['button'], handler: 'onClose' }"}],staticClass:"header-auth-wrapper"},[n("v-btn",{ref:"button",staticClass:"header-auth",attrs:{text:"",rounded:""}},[n("v-avatar",{attrs:{size:"10rem"},on:{click:function(t){e.overlay=!e.overlay}}},[e.user.picture?n("img",{attrs:{src:e.user.picture,alt:e.user.name}}):n("div",{staticClass:"header-auth__anonymous"},[n("v-icon",{attrs:{size:"6rem",color:"secondary"}},[e._v(e._s(e.iconUser))])],1)])],1),e.user?n("v-overlay",{attrs:{absolute:!0,color:"",value:e.overlay}},[n("v-card",{attrs:{light:""}},[n("div",{staticClass:"pa-6"},[n("v-icon",{staticClass:"dialog-close",attrs:{large:"",color:"black"},on:{click:function(t){e.overlay=!1}}},[e._v(e._s(e.iconClose)+" ")]),n("v-card-text",{staticClass:"text-center pa-0"},[n("v-avatar",{staticClass:"mb-6",attrs:{size:"13rem"}},[e.user.picture?n("img",{attrs:{src:e.user.picture,alt:e.user.name}}):n("div",{staticClass:"header-auth__anonymous"},[n("v-icon",{attrs:{size:"10rem",color:"secondary"}},[e._v(e._s(e.iconUser))])],1)]),e.user.name?n("h3",[e._v(e._s(e.user.name))]):e._e(),e.user.email?n("p",{staticClass:"body-3 mt-2 mb-8"},[e._v(e._s(e.user.email))]):n("p",{staticClass:"body-3 mt-2 mb-8"},[e._v("Welcome to "),n("strong",[e._v("Pickee!")])]),n("div",{staticClass:"pl-12 pr-12 ml-12 mr-12 pl-p-0 pr-p-0 ml-p-0 mr-p-0"},[e.user.id?[n("v-btn",{staticClass:"mb-4 pl-6 pr-6",attrs:{block:"",color:"primary",href:"/profile/"}},[e._v("Manage account ")]),n("v-btn",{attrs:{block:"",outlined:"",href:"/logout/"}},[e._v("Logout")])]:[n("v-btn",{staticClass:"mb-4",attrs:{block:"",color:"primary",href:"/login/"}},[e._v("Login ")]),n("v-btn",{staticClass:"pl-6 pr-6",attrs:{block:"",outlined:"",href:"/signup/"}},[e._v("Create account")])]],2)],1)],1)])],1):e._e()],1)},f=[],p=(n("4160"),n("159b"),n("2b0e")),m=n("94ed");p["a"].directive("closable",{bind:function(e,t,n){a=function(a){a.stopPropagation();var r=t.value,o=r.handler,s=r.exclude,i=!1;s.forEach((function(e){if(!i){var t=n.context.$refs[e];i=t.$el.contains(a.target)}})),e.contains(a.target)||i||n.context[o]()},document.addEventListener("click",a),document.addEventListener("touchstart",a)},unbind:function(){document.removeEventListener("click",a),document.removeEventListener("touchstart",a)}});var b={name:"HeaderAuth",props:["user"],methods:{onClose:function(){this.overlay=!1}},data:function(){return{overlay:!1,iconUser:m["a"],iconClose:m["f"]}}},g=b,y=(n("604d"),n("6544")),_=n.n(y),x=n("8212"),w=n("8336"),k=n("b0af"),C=n("99d9"),S=n("132d"),E=n("a797"),P=Object(u["a"])(g,h,f,!1,null,null,null),U=P.exports;_()(P,{VAvatar:x["a"],VBtn:w["a"],VCard:k["a"],VCardText:C["b"],VIcon:S["a"],VOverlay:E["a"]});var O=n("e532"),F={name:"PageHeader",props:{logo:Boolean,isAboutPage:Boolean,user:Object},components:{Navigation:v,HeaderAuth:U,Logo:O["a"]}},j=F,A=(n("0426"),Object(u["a"])(j,r,o,!1,null,null,null));t["a"]=A.exports},2627:function(e,t,n){},3:function(e,t,n){e.exports=n("9396")},"4a60":function(e,t,n){"use strict";var a=n("be45"),r=n.n(a);r.a},"604d":function(e,t,n){"use strict";var a=n("ea03"),r=n.n(a);r.a},"8a71":function(e,t,n){},9396:function(e,t,n){"use strict";n.r(t);var a=n("2b0e"),r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app",[n("div",{staticClass:"page-wrapper"},[n("PageHeader",{attrs:{logo:""}}),n("v-content",{staticClass:"page-content page-content--centered"},[n("SignUpBox",{attrs:{actionUrl:e.actionUrl,loginUrl:e.loginUrl,data:e.data}})],1)],1)])},o=[],s=n("1269"),i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-card",{staticClass:"auth-box",attrs:{light:""}},[n("h1",{staticClass:"auth-box__header"},[e._v("Sign Up")]),e.data.errors?n("div",{staticClass:"auth-box__errors"},[e._l(e.data.errors,(function(t,a){return[e._l(t,(function(t){return[n("p",{key:a+t},[e._v(e._s(a)+": "+e._s(t))])]}))]}))],2):e._e(),n("form",{attrs:{method:"post",action:e.actionUrl}},[n("input",{attrs:{type:"hidden",name:"csrfmiddlewaretoken"},domProps:{value:e.token}}),n("FormTextField",{attrs:{type:"text",label:"Email",name:"email"}}),n("FormTextField",{attrs:{type:"password",label:"Password",name:"password1"}}),n("FormTextField",{attrs:{type:"password",label:"Password confirmation",name:"password2"}}),n("v-btn",{staticClass:"auth-box__submit",attrs:{type:"submit",color:"primary"}},[e._v("Sign Up")])],1),n("a",{staticClass:"auth-box__signup-link",attrs:{href:e.loginUrl}},[e._v("Login")])])},l=[],c=n("af01"),u={name:"LoginBox",data:function(){return{token:this.$cookies.get("csrftoken")}},props:["actionUrl","loginUrl","data"],components:{FormTextField:c["a"]}},d=u,v=n("2877"),h=n("6544"),f=n.n(h),p=n("8336"),m=n("b0af"),b=Object(v["a"])(d,i,l,!1,null,null,null),g=b.exports;f()(b,{VBtn:p["a"],VCard:m["a"]});var y={name:"SignUp",data:function(){return{actionUrl:"",loginUrl:"",data:{}}},methods:{},components:{PageHeader:s["a"],SignUpBox:g},beforeMount:function(){var e=document.getElementsByTagName("app")[0];this.actionUrl=e.getAttribute("actionUrl"),this.loginUrl=e.getAttribute("loginUrl");var t=e.getAttribute("data");t&&(this.data=JSON.parse(t))}},_=y,x=n("7496"),w=n("a75b"),k=Object(v["a"])(_,r,o,!1,null,null,null),C=k.exports;f()(k,{VApp:x["a"],VContent:w["a"]});var S=n("b8e3"),E=n("0532"),P=n("2b27"),U=n.n(P);n("8a71");a["a"].use(U.a),new E["a"],a["a"].config.productionTip=!1,new a["a"]({vuetify:S["a"],render:function(e){return e(C)}}).$mount("#signup")},aee1:function(e,t,n){"use strict";var a=n("d01a"),r=n.n(a);r.a},af01:function(e,t,n){"use strict";var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"form-text-field",class:{"form-text-field--horizontal":e.horizontal}},[n("label",{staticClass:"label"},[e._v(e._s(e.label))]),n("v-text-field",{attrs:{placeholder:e.placeholder,name:e.name,type:e.type,solo:"",dark:""},on:{change:function(t){e.changeEvent&&e.changeEvent(e.name,e.model)}},model:{value:e.model,callback:function(t){e.model=t},expression:"model"}})],1)},r=[],o={name:"FormTextField",props:{label:String,name:String,type:String,placeholder:String,horizontal:Boolean,value:String,changeEvent:Function},data:function(){return{model:this.value}},watch:{model:function(){this.$emit("input",this.model)}}},s=o,i=(n("aee1"),n("2877")),l=n("6544"),c=n.n(l),u=n("8654"),d=Object(i["a"])(s,a,r,!1,null,null,null);t["a"]=d.exports;c()(d,{VTextField:u["a"]})},b8e3:function(e,t,n){"use strict";var a=n("2b0e"),r=n("f309"),o={primary:"#ffbf69",secondary:"#2d3142",red:"#FF6969",green:"#69FF80",grey100:"#fbfbfb",grey200:"#eaeaea",grey300:"#d3d0c5",grey400:"#a8a8a8",grey500:"#a0a0a0",grey700:"#4b4b4b",grey800:"#363636",grey950:"#282828",grey960:"#262626",grey970:"#242424",grey985:"#2b2b2b",grey980:"#191919",grey990:"#151515",bodyText:"#fbfbfb",bodyBg:"#242424"};a["a"].use(r["a"]);var s={theme:{themes:{dark:o},dark:!0,options:{customProperties:!0}},icons:{iconfont:"mdiSvg"}};t["a"]=new r["a"](s)},be45:function(e,t,n){},d01a:function(e,t,n){},e532:function(e,t,n){"use strict";var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("a",{staticClass:"logo",attrs:{href:"/"}},[e._v("Pickee")])},r=[],o=(n("4a60"),n("2877")),s={},i=Object(o["a"])(s,a,r,!1,null,null,null);t["a"]=i.exports},ea03:function(e,t,n){}});