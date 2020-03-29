(function(e){function t(t){for(var r,i,o=t[0],c=t[1],u=t[2],d=0,m=[];d<o.length;d++)i=o[d],Object.prototype.hasOwnProperty.call(a,i)&&a[i]&&m.push(a[i][0]),a[i]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(e[r]=c[r]);l&&l(t);while(m.length)m.shift()();return s.push.apply(s,u||[]),n()}function n(){for(var e,t=0;t<s.length;t++){for(var n=s[t],r=!0,o=1;o<n.length;o++){var c=n[o];0!==a[c]&&(r=!1)}r&&(s.splice(t--,1),e=i(i.s=n[0]))}return e}var r={},a={Recommendation:0},s=[];function i(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,i),n.l=!0,n.exports}i.m=e,i.c=r,i.d=function(e,t,n){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(i.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)i.d(n,r,function(t){return e[t]}.bind(null,r));return n},i.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],c=o.push.bind(o);o.push=t,o=o.slice();for(var u=0;u<o.length;u++)t(o[u]);var l=c;s.push([8,"chunk-vendors"]),n()})({"0426":function(e,t,n){"use strict";var r=n("2627"),a=n.n(r);a.a},"0532":function(e,t,n){"use strict";n.d(t,"a",(function(){return l}));n("4160");var r=n("d4ec"),a=n("bee2"),s=n("c6c6"),i=n.n(s),o={desktop:1920,tablet:768,phone:320},c=1024,u=10,l=function(){function e(){Object(r["a"])(this,e),this.md=new i.a(window.navigator.userAgent),this.$html=document.documentElement,this.$window=window,this.device,this.init()}return Object(a["a"])(e,[{key:"init",value:function(){this.device=this.detectDevice(),this.runScreenResize(),this.bindEvents()}},{key:"detectDevice",value:function(){var e="desktop";return this.md.tablet()?e="tablet":this.md.mobile()&&(e="phone"),e}},{key:"bindEvents",value:function(){var e=this;this.$window.addEventListener("resize",(function(){e.switchBodyClasses(),e.changeBaseFontSize()}))}},{key:"runScreenResize",value:function(){this.switchBodyClasses(),this.changeBaseFontSize()}},{key:"changeBaseFontSize",value:function(){var e=this.calcBaseWidth(),t=this.calculateFontSize(e);this.setPageFontSize(t)}},{key:"calcBaseWidth",value:function(){return o[this.device]}},{key:"calculateFontSize",value:function(e){var t=document.documentElement.clientWidth;t="tablet"===this.device?Math.min(this.$window.innerWidth,e):Math.min(Math.max(this.$window.innerWidth,c),e);var n=t/e*u+"px";return n}},{key:"getTargetWidth",value:function(){return Math.min(this.$window.innerWidth(),o)}},{key:"setPageFontSize",value:function(e){this.$html.style.fontSize=e}},{key:"switchBodyClasses",value:function(){var e=document.body,t=["desktop","tablet","phone"];t.forEach((function(t){return e.classList.remove(t)})),e.classList.add(this.device)}}]),e}()},"0d87":function(e,t,n){},"121a":function(e,t,n){"use strict";var r=n("7f05"),a=n.n(r);a.a},1269:function(e,t,n){"use strict";var r,a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("header",{staticClass:"page-header"},[e.logo?n("Logo"):e._e(),n("Navigation",{attrs:{isAboutPage:e.isAboutPage}}),e.user?n("HeaderAuth",{attrs:{user:e.user}}):e._e()],1)},s=[],i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("nav",{staticClass:"header-nav"},[e.isAboutPage?e._e():n("a",{staticClass:"link",attrs:{href:"/about/"}},[e._v("About Us")]),e.isAboutPage?n("a",{staticClass:"link",attrs:{href:"/"}},[e._v("Home")]):e._e()])},o=[],c={name:"Navigation",props:{isAboutPage:Boolean}},u=c,l=n("2877"),d=Object(l["a"])(u,i,o,!1,null,null,null),m=d.exports,p=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{directives:[{name:"closable",rawName:"v-closable",value:{exclude:["button"],handler:"onClose"},expression:"{ exclude: ['button'], handler: 'onClose' }"}],staticClass:"header-auth-wrapper"},[n("v-btn",{ref:"button",staticClass:"header-auth",attrs:{text:"",rounded:""}},[n("v-avatar",{attrs:{size:"10rem"},on:{click:function(t){e.overlay=!e.overlay}}},[e.user.picture?n("img",{attrs:{src:e.user.picture,alt:e.user.name}}):n("div",{staticClass:"header-auth__anonymous"},[n("v-icon",{attrs:{size:"6rem",color:"secondary"}},[e._v(e._s(e.iconUser))])],1)])],1),e.user?n("v-overlay",{attrs:{absolute:!0,color:"",value:e.overlay}},[n("v-card",{attrs:{light:""}},[n("div",{staticClass:"pa-6"},[n("v-icon",{staticClass:"dialog-close",attrs:{large:"",color:"black"},on:{click:function(t){e.overlay=!1}}},[e._v(e._s(e.iconClose)+" ")]),n("v-card-text",{staticClass:"text-center pa-0"},[n("v-avatar",{staticClass:"mb-6",attrs:{size:"13rem"}},[e.user.picture?n("img",{attrs:{src:e.user.picture,alt:e.user.name}}):n("div",{staticClass:"header-auth__anonymous"},[n("v-icon",{attrs:{size:"10rem",color:"secondary"}},[e._v(e._s(e.iconUser))])],1)]),e.user.name?n("h3",[e._v(e._s(e.user.name))]):e._e(),e.user.email?n("p",{staticClass:"body-3 mt-2 mb-8"},[e._v(e._s(e.user.email))]):n("p",{staticClass:"body-3 mt-2 mb-8"},[e._v("Welcome to "),n("strong",[e._v("Pickee!")])]),n("div",{staticClass:"pl-12 pr-12 ml-12 mr-12 pl-p-0 pr-p-0 ml-p-0 mr-p-0"},[e.user.id?[n("v-btn",{staticClass:"mb-4 pl-6 pr-6",attrs:{block:"",color:"primary",href:"/profile/"}},[e._v("Manage account ")]),n("v-btn",{attrs:{block:"",outlined:"",href:"/logout/"}},[e._v("Logout")])]:[n("v-btn",{staticClass:"mb-4",attrs:{block:"",color:"primary",href:"/login/"}},[e._v("Login ")]),n("v-btn",{staticClass:"pl-6 pr-6",attrs:{block:"",outlined:"",href:"/signup/"}},[e._v("Create account")])]],2)],1)],1)])],1):e._e()],1)},v=[],f=(n("4160"),n("159b"),n("2b0e")),h=n("94ed");f["a"].directive("closable",{bind:function(e,t,n){r=function(r){r.stopPropagation();var a=t.value,s=a.handler,i=a.exclude,o=!1;i.forEach((function(e){if(!o){var t=n.context.$refs[e];o=t.$el.contains(r.target)}})),e.contains(r.target)||o||n.context[s]()},document.addEventListener("click",r),document.addEventListener("touchstart",r)},unbind:function(){document.removeEventListener("click",r),document.removeEventListener("touchstart",r)}});var g={name:"HeaderAuth",props:["user"],methods:{onClose:function(){this.overlay=!1}},data:function(){return{overlay:!1,iconUser:h["a"],iconClose:h["f"]}}},b=g,w=(n("604d"),n("6544")),_=n.n(w),x=n("8212"),R=n("8336"),k=n("b0af"),y=n("99d9"),C=n("132d"),O=n("a797"),j=Object(l["a"])(b,p,v,!1,null,null,null),D=j.exports;_()(j,{VAvatar:x["a"],VBtn:R["a"],VCard:k["a"],VCardText:y["b"],VIcon:C["a"],VOverlay:O["a"]});var L=n("e532"),E={name:"PageHeader",props:{logo:Boolean,isAboutPage:Boolean,user:Object},components:{Navigation:m,HeaderAuth:D,Logo:L["a"]}},S=E,P=(n("0426"),Object(l["a"])(S,a,s,!1,null,null,null));t["a"]=P.exports},2627:function(e,t,n){},3062:function(e,t,n){"use strict";var r=n("9d48"),a=n.n(r);a.a},"49fe":function(e,t,n){},"4a60":function(e,t,n){"use strict";var r=n("be45"),a=n.n(r);a.a},"4cac":function(e,t,n){"use strict";var r=n("0d87"),a=n.n(r);a.a},"604d":function(e,t,n){"use strict";var r=n("ea03"),a=n.n(r);a.a},7424:function(e,t,n){"use strict";n("99af"),n("7db0"),n("4160"),n("c975"),n("159b"),n("96cf");var r=n("1da1"),a=(n("d3b7"),n("2b27")),s=n.n(a),i="/api",o=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t,n,r){var a,o,c;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return a=new Headers,a.append("X-CSRFToken",s.a.get("csrftoken")),a.append("Content-Type","application/json"),o={method:r||"POST",headers:a},n&&(o.body=JSON.stringify(n)),e.next=7,fetch(i+t,o);case 7:return c=e.sent,e.next=10,c.text().then((function(e){return e?JSON.parse(e):{}}));case 10:return e.abrupt("return",e.sent);case 11:case"end":return e.stop()}}),e)})));return function(t,n,r){return e.apply(this,arguments)}}(),c=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t,n,r,a){var o,c,u,l;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return o=new FormData,o.append(n,r),c=new Headers,c.append("X-CSRFToken",s.a.get("csrftoken")),u={method:a||"POST",headers:c,body:o},e.next=7,fetch(i+t,u);case 7:return l=e.sent,e.next=10,l.text().then((function(e){return e?JSON.parse(e):{}}));case 10:return e.abrupt("return",e.sent);case 11:case"end":return e.stop()}}),e)})));return function(t,n,r,a){return e.apply(this,arguments)}}(),u=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,o(t,null,"DELETE");case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),l=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t,n){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,o(t,n,"PUT");case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(t,n){return e.apply(this,arguments)}}(),d=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t,n){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,o(t,n,"POST");case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(t,n){return e.apply(this,arguments)}}(),m=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,o(t,null,"GET");case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),p=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t,n){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,o(t,n,"PATCH");case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(t,n){return e.apply(this,arguments)}}(),v=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t,n,a){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:a.forEach(function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(r){var a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(n.find((function(e){return e.genre===r}))){e.next=4;break}return a={user:t,genre:r},e.next=4,d("/users/".concat(t,"/favorite-genres/"),a);case 4:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}());case 1:case"end":return e.stop()}}),e)})));return function(t,n,r){return e.apply(this,arguments)}}(),f=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t,n,a){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:n.forEach(function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(n){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(-1!==a.indexOf(n.genre)){e.next=3;break}return e.next=3,u("/users/".concat(t,"/favorite-genres/").concat(n.id));case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}());case 1:case"end":return e.stop()}}),e)})));return function(t,n,r){return e.apply(this,arguments)}}();t["a"]={createSession:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){var n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n={users:e},t.next=3,d("/sessions/",n);case 3:return t.abrupt("return",t.sent);case 4:case"end":return t.stop()}}),t)})))()},getGenres:function(){return Object(r["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,m("/genres/");case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})))()},getFavoriteGenres:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/users/".concat(e,"/favorite-genres/"));case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})))()},updateFavoriteGenres:function(e,t,n){return Object(r["a"])(regeneratorRuntime.mark((function r(){var a;return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return r.next=2,m("/users/".concat(e,"/favorite-genres/"));case 2:a=r.sent,n?v(e,a,t):f(e,a,t);case 4:case"end":return r.stop()}}),r)})))()},getUser:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/users/?email=".concat(e));case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})))()},getAscUsers:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){var n,r,a,s,i;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/users/".concat(e,"/"));case 2:n=t.sent,r=[],a=n.associated_users,s=0;case 6:if(!(s<a.length)){t.next=14;break}return t.next=9,m("/users/".concat(a[s],"/"));case 9:i=t.sent,r.push(i);case 11:s++,t.next=6;break;case 14:return t.abrupt("return",r);case 15:case"end":return t.stop()}}),t)})))()},saveAscUsers:function(e,t){return Object(r["a"])(regeneratorRuntime.mark((function n(){var r;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return r={associated_users:t},n.next=3,p("/users/".concat(e,"/"),r);case 3:return n.abrupt("return",n.sent);case 4:case"end":return n.stop()}}),n)})))()},getFavoriteActors:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/users/".concat(e,"/favorite-actors/"));case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})))()},addFavoriteActors:function(e,t){return Object(r["a"])(regeneratorRuntime.mark((function n(){var r,a,s,i,o;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:r=[],a=0;case 2:if(!(a<t.length)){n.next=18;break}return s=t[a].actor,n.next=6,m("/actors/".concat(s.id));case 6:if(i=n.sent,i.id){n.next=14;break}return n.next=10,d("/actors/",s);case 10:o=n.sent,r.push({user:e,actor:o.id}),n.next=15;break;case 14:r.push({user:e,actor:s.id});case 15:a++,n.next=2;break;case 18:return n.next=20,d("/users/".concat(e,"/favorite-actors/"),r);case 20:return n.abrupt("return",n.sent);case 21:case"end":return n.stop()}}),n)})))()},getActor:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/actors/".concat(e));case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})))()},searchActor:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/search/actors/?name=".concat(e));case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})))()},removeFavoriteActors:function(e,t){return Object(r["a"])(regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return n.next=2,u("/users/".concat(e,"/favorite-actors/").concat(t,"/"));case 2:return n.abrupt("return",n.sent);case 3:case"end":return n.stop()}}),n)})))()},getFavoriteMovies:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/users/".concat(e,"/favorite-movies/"));case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})))()},addFavoriteMovies:function(e,t){return Object(r["a"])(regeneratorRuntime.mark((function n(){var r,a,s,i,o;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:r=[],a=0;case 2:if(!(a<t.length)){n.next=18;break}return s=t[a].movie,n.next=6,m("/movies/".concat(s.id));case 6:if(i=n.sent,i.id){n.next=14;break}return n.next=10,d("/movies/",s);case 10:o=n.sent,r.push({user:e,movie:o.id}),n.next=15;break;case 14:r.push({user:e,movie:s.id});case 15:a++,n.next=2;break;case 18:return n.next=20,d("/users/".concat(e,"/favorite-movies/"),r);case 20:return n.abrupt("return",n.sent);case 21:case"end":return n.stop()}}),n)})))()},removeFavoriteMovies:function(e,t){return Object(r["a"])(regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return n.next=2,u("/users/".concat(e,"/favorite-movies/").concat(t,"/"));case 2:return n.abrupt("return",n.sent);case 3:case"end":return n.stop()}}),n)})))()},searchMovie:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/search/movies/?name=".concat(e));case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})))()},getMovie:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/movies/".concat(e));case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})))()},updateUserProfile:function(e,t){return Object(r["a"])(regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return n.next=2,p("/users/".concat(e,"/"),t);case 2:return n.abrupt("return",n.sent);case 3:case"end":return n.stop()}}),n)})))()},getRecommendation:function(e,t,n){return Object(r["a"])(regeneratorRuntime.mark((function r(){var a;return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return a={runtime:e.runtime,genre_ids:e.genre_ids,user_ids:e.user_ids,offset:n},t&&(a.session_id=t),r.next=4,d("/recommendations/generate",a);case 4:return r.abrupt("return",r.sent);case 5:case"end":return r.stop()}}),r)})))()},setRecommendationUserChoice:function(e,t,n,a){return Object(r["a"])(regeneratorRuntime.mark((function r(){var s;return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return s={user_choice:a,movie:n,session:t},r.next=3,l("/recommendations/".concat(e,"/"),s);case 3:return r.abrupt("return",r.sent);case 4:case"end":return r.stop()}}),r)})))()},getProviderList:function(e){return Object(r["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,m("/providers/?movie_name=".concat(e));case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})))()},updateAvatar:function(e,t){return Object(r["a"])(regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return n.next=2,c("/users/".concat(e,"/"),"picture",t,"PATCH");case 2:return n.abrupt("return",n.sent);case 3:case"end":return n.stop()}}),n)})))()}}},"7f05":function(e,t,n){},8:function(e,t,n){e.exports=n("becc")},"8a71":function(e,t,n){},"9d48":function(e,t,n){},a337:function(e,t,n){"use strict";var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("ul",{staticClass:"item-list",class:{"item-list--accented":e.accented}},[e._l(e.items,(function(t){return[n("li",{key:t.id,staticClass:"item-list__element"},[n("button",{staticClass:"item-list__element-button",on:{click:function(n){return e.buttonAction(t)}}},[t.image?n("v-avatar",{staticClass:"item-list__element-avatar",attrs:{size:"6.8rem"}},[n("img",{attrs:{src:t.image,alt:t.text}})]):t.picture?n("img",{staticClass:"item-list__element-picture",attrs:{src:t.picture,alt:t.text}}):e._e(),t.logo?n("div",{staticClass:"item-list__element-logo"},[n("img",{attrs:{src:t.logo,alt:t.text}})]):e._e(),n("span",{staticClass:"item-list__element-text"},[e._v(e._s(t.text))]),t.icon?n("v-icon",{staticClass:"item-list__element-icon"},[e._v(e._s(t.icon))]):e._e()],1)])]}))],2)},a=[],s={name:"ItemList",props:{items:Array,buttonAction:Function,accented:Boolean}},i=s,o=(n("4cac"),n("2877")),c=n("6544"),u=n.n(c),l=n("8212"),d=n("132d"),m=Object(o["a"])(i,r,a,!1,null,null,null);t["a"]=m.exports;u()(m,{VAvatar:l["a"],VIcon:d["a"]})},b8e3:function(e,t,n){"use strict";var r=n("2b0e"),a=n("f309"),s={primary:"#ffbf69",secondary:"#2d3142",red:"#FF6969",green:"#69FF80",grey100:"#fbfbfb",grey200:"#eaeaea",grey300:"#d3d0c5",grey400:"#a8a8a8",grey500:"#a0a0a0",grey700:"#4b4b4b",grey800:"#363636",grey950:"#282828",grey960:"#262626",grey970:"#242424",grey985:"#2b2b2b",grey980:"#191919",grey990:"#151515",bodyText:"#fbfbfb",bodyBg:"#242424"};r["a"].use(a["a"]);var i={theme:{themes:{dark:s},dark:!0,options:{customProperties:!0}},icons:{iconfont:"mdiSvg"}};t["a"]=new a["a"](i)},be45:function(e,t,n){},becc:function(e,t,n){"use strict";n.r(t);var r=n("2b0e"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app",[n("div",{staticClass:"page-wrapper page-recommendation"},[n("PageHeader",{attrs:{user:e.user,logo:""}}),n("v-content",[n("RecommendationBox",{attrs:{user:e.user,preferences:e.preferences}})],1)],1)])},s=[],i=n("1269"),o=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"recommendation-box"},[n("v-btn",{staticClass:"recommendation-box__goback",attrs:{color:"secondary",href:"/?step=2"}},[e._v("Back to preferences")]),e.isInitialLoading?n("div",{staticClass:"mx-auto mt-p-12"},[n("v-progress-circular",{attrs:{size:140,width:7,color:"primary",indeterminate:""}})],1):e._e(),!e.isInitialLoading&&e.recData.id?[n("RecommendationCarousel",{ref:"recCarousel",attrs:{activeSlideIndex:e.activeRecIndex,recommendation:e.recData,isLoading:e.isLoading,showPrevRec:e.showPrevRec,showNextRec:e.showNextRec}}),n("RecommendationDescr",{attrs:{recommendation:e.recData,providerList:e.providerList,newRecEvent:e.getNewRecommendation,acceptEvent:e.getProviderList,isLoading:e.isLoading}})]:e._e(),n("v-dialog",{attrs:{width:"84rem",persistent:!0},model:{value:e.noResultsDialog,callback:function(t){e.noResultsDialog=t},expression:"noResultsDialog"}},[n("v-card",{attrs:{light:""}},[n("div",{staticClass:"px-8 py-6 py-p-3 px-p-4"},[n("v-icon",{staticClass:"dialog-close",attrs:{large:"",color:"black"},on:{click:function(t){e.noResultsDialog=!1}}},[e._v(e._s(e.iconClose))]),n("v-card-text",{staticClass:"pt-12 my-12 py-12 px-p-0"},[n("h3",{staticClass:"pt-6 mb-6 text-center"},[e._v("Whoaaaah! You are too pickee. You should come and work for us.")]),n("p",{},[e._v("Unfortunately your preferences are a bit too narrow, please come back and edit them to get fresh recommendations :)")])]),n("v-card-actions",{staticClass:"dialog-actions d-flex justify-space-between"},[n("button",{staticClass:"dialog-actions__button",on:{click:e.navigateBackToHome}},[e._v("Return to home page")]),e.recData?n("button",{staticClass:"dialog-actions__button",on:{click:function(t){e.noResultsDialog=!1}}},[e._v("Done")]):e._e()])],1)])],1)],2)},c=[],u=(n("99af"),n("4de4"),n("d81d"),n("b0c0"),n("b64b"),n("ac1f"),n("5319"),n("1276"),n("2909")),l=(n("96cf"),n("1da1")),d=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"recommendation-carousel"},[n("swiper",{ref:"mySwiper",staticClass:"recommendation-carousel__swiper",attrs:{options:e.swiperOption}},e._l(e.swiperSlides,(function(t){return n("swiper-slide",{key:t.recommendationID,staticClass:"recommendation-carousel__swiper-slide"},["REJECTED"===t.user_choice?n("div",{staticClass:"action-button"},[n("v-icon",{attrs:{color:"red",size:"4.5rem"}},[e._v(e._s(e.iconThumbDown))])],1):e._e(),"BOOKMARKED"===t.user_choice?n("div",{staticClass:"action-button"},[n("v-icon",{attrs:{color:"primary",size:"4.5rem"}},[e._v(e._s(e.iconFavorites))])],1):e._e(),"ACCEPTED"===t.user_choice?n("div",{staticClass:"action-button"},[n("v-icon",{attrs:{color:"green",size:"4.5rem"}},[e._v(e._s(e.iconThumbUp))])],1):e._e(),t.image_url?n("img",{attrs:{src:t.image_url,alt:t.name}}):n("div",{staticClass:"recommendation-carousel__empty-poster"},[n("span",[e._v("Poster not yet available")])])])})),1),n("button",{staticClass:"recommendation-carousel__swiper-button-prev",attrs:{slot:"button-prev"},on:{click:e.showPrevRec},slot:"button-prev"},[n("v-icon",{attrs:{size:"6.5rem"}},[e._v(e._s(e.iconArrowLeft))])],1),n("button",{staticClass:"recommendation-carousel__swiper-button-next",attrs:{slot:"button-next"},on:{click:e.showNextRec},slot:"button-next"},[n("v-icon",{attrs:{size:"6.5rem"}},[e._v(e._s(e.iconArrowRight))])],1)],1)},m=[],p=(n("dfa4"),n("7212")),v=n("94ed"),f={name:"RecommendationCarousel",props:["recommendation","isLoading","showPrevRec","showNextRec","activeSlideIndex"],components:{swiper:p["swiper"],swiperSlide:p["swiperSlide"]},methods:{setNewRecommendation:function(e,t){var n=this;if(this.swiperSlides[this.activeSlideIndex].user_choice=t,"ACCEPTED"===t)return!1;e&&(this.swiperSlides.push({recommendationID:e.recommendation_id,image_url:e.image_url,name:e.name,user_choice:null}),setTimeout((function(){n.$refs.mySwiper.swiper.slideTo(n.swiperSlides.length-1)}),100))}},mounted:function(){this.swiperSlides.push({image_url:this.recommendation.image_url,name:this.recommendation.name,user_choice:null})},data:function(){return{iconArrowLeft:v["d"],iconArrowRight:v["e"],iconFavorites:v["c"],iconThumbDown:v["o"],iconThumbUp:v["p"],swiperSlides:[],swiperOption:{effect:"coverflow",centeredSlides:!0,initialSlide:1,slidesPerView:"auto",spaceBetween:0,grabCursor:!1,simulateTouch:!1,navigation:{nextEl:".recommendation-carousel__swiper-button-next",prevEl:".recommendation-carousel__swiper-button-prev"},coverflowEffect:{rotate:0,stretch:0,depth:20,modifier:20,slideShadows:!1}}}}},h=f,g=(n("ea98"),n("2877")),b=n("6544"),w=n.n(b),_=n("132d"),x=Object(g["a"])(h,d,m,!1,null,null,null),R=x.exports;w()(x,{VIcon:_["a"]});var k=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"recommendation-descr"},[n("v-card",[n("v-card-text",[n("div",{staticClass:"recommendation-descr__top"},[e.recommendation.rating>0?n("v-progress-circular",{staticClass:"recommendation-descr__rating",attrs:{value:10*e.recommendation.rating,rotate:"270",width:"2.5",color:"primary"}},[e._v(e._s(e.recommendation.rating))]):e._e(),n("div",{staticClass:"recommendation-descr__heading"},[n("h2",{staticClass:"recommendation-descr__title"},[e._v(e._s(e.recommendation.name))]),n("p",{staticClass:"recommendation-descr__date"},[e._v(e._s(e.recMovieReleaseDate))])])],1),n("div",{staticClass:"recommendation-descr__text"},[n("h3",{staticClass:"recommendation-descr__text-heading"},[e._v("Overview")]),n("p",[e._v(e._s(e.recommendation.description))])]),n("div",{staticClass:"recommendation-descr__text"},[n("h3",{staticClass:"recommendation-descr__text-heading"},[e._v("Featured Crew")]),n("p",e._l(e.recommendation.cast,(function(t){return n("span",{key:t.id,staticClass:"recommendation-descr__text-item"},[e._v(e._s(t.name))])})),0)])])],1),n("div",{staticClass:"recommendation-descr__actions"},[n("button",{staticClass:"action-button",attrs:{disabled:e.isLoading},on:{click:function(t){return e.newRecEvent("REJECTED")}}},[n("v-icon",{attrs:{color:"red",size:"7.5rem"}},[e._v(e._s(e.iconThumbDown))])],1),n("button",{staticClass:"action-button",attrs:{disabled:e.isLoading},on:{click:function(t){return e.newRecEvent("BOOKMARKED")}}},[n("v-icon",{attrs:{color:"primary",size:"7.5rem"}},[e._v(e._s(e.iconFavorites))])],1),n("v-dialog",{attrs:{width:"84rem",persistent:!0},scopedSlots:e._u([{key:"activator",fn:function(t){var r=t.on;return[n("button",e._g({staticClass:"action-button",attrs:{disabled:e.isLoading},on:{click:function(t){return e.acceptEvent("ACCEPTED")}}},r),[n("v-icon",{attrs:{color:"green",size:"7.5rem"}},[e._v(e._s(e.iconThumbUp))])],1)]}}]),model:{value:e.dialog,callback:function(t){e.dialog=t},expression:"dialog"}},[n("v-card",{attrs:{light:""}},[n("div",{staticClass:"px-8 py-6 py-p-3 px-p-4"},[n("v-icon",{staticClass:"dialog-close",attrs:{large:"",color:"black"},on:{click:function(t){e.dialog=!1}}},[e._v(e._s(e.iconClose))]),n("v-card-text",{staticClass:"px-12 pb-4 px-p-0"},[e.isLoading?n("div",{staticClass:"pa-12 text-center"},[n("v-progress-circular",{attrs:{size:70,width:5,color:"secondary",indeterminate:""}})],1):[e.providerList.length>0?[n("p",{staticClass:"recommendation-descr__popup-text"},[n("strong",[e._v("Yessssss!")]),e._v(" Habemus movie. Now go ahead and watch it.")]),n("ItemList",{attrs:{items:e.providerList,"button-action":e.openProvider}})]:n("p",{staticClass:"recommendation-descr__popup-text pb-0"},[e._v("Sorry, but we don't know any available providers for this movie/show :(")])]],2)],1)])],1)],1)],1)},y=[],C=(n("9911"),n("a337")),O={name:"RecommendationDescr",props:["recommendation","newRecEvent","acceptEvent","providerList","isLoading"],components:{ItemList:C["a"]},methods:{openProvider:function(e){window.open(e.link)}},computed:{recMovieReleaseDate:function(){var e=new Date(this.recommendation.release_date),t=e.getDate(),n=e.getMonth(),r=e.getFullYear();return"".concat(t,".").concat(n,".").concat(r)}},data:function(){return{iconFavorites:v["c"],iconThumbDown:v["o"],iconThumbUp:v["p"],iconClose:v["f"],ratingValue:74,dialog:!1}}},j=O,D=(n("3062"),n("b0af")),L=n("99d9"),E=n("169a"),S=n("490a"),P=Object(g["a"])(j,k,y,!1,null,null,null),A=P.exports;w()(P,{VCard:D["a"],VCardText:L["b"],VDialog:E["a"],VIcon:_["a"],VProgressCircular:S["a"]});var T=n("7424"),I={name:"RecommendationBox",props:["preferences","user","setNewRecommendation"],data:function(){return{data:{},recData:{},token:this.$cookies.get("csrftoken"),sessionID:null,offset:1,providerList:[],isInitialLoading:!0,isLoading:!1,noResultsDialog:!1,recommendationList:[],activeRecIndex:0,lastRecIndex:0,iconClose:v["f"]}},created:function(){var e=Object(l["a"])(regeneratorRuntime.mark((function e(){var t,n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(!this.user.id){e.next=6;break}return this.preferences.user_ids=[this.user.id+""].concat(Object(u["a"])(this.preferences.user_ids.split(",").filter((function(e){return""!=e})))),e.next=4,T["a"].createSession(this.preferences.user_ids);case 4:t=e.sent,this.sessionID=t.id;case 6:return e.next=8,T["a"].getRecommendation(this.preferences,this.sessionID,0);case 8:n=e.sent,this.recommendationList.push(n),n.results&&0===n.total_results?(this.noResultsDialog=!0,this.recData=null):(this.recData=this.recommendationList[this.lastRecIndex],this.isInitialLoading=!1);case 11:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}(),methods:{navigateBackToHome:function(){window.location.replace("/?step=2")},getNewRecommendation:function(){var e=Object(l["a"])(regeneratorRuntime.mark((function e(t){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return this.isLoading=!0,this.updateRecommendationStatus(t),e.next=4,T["a"].getRecommendation(this.preferences,this.sessionID,this.offset);case 4:n=e.sent,this.offset++,n&&n!={}&&0!==Object.keys(n).length?(this.recommendationList.push(n),this.isLoading=!1):this.noResultsDialog=!0,this.recData=this.recommendationList[++this.lastRecIndex],this.activeRecIndex=this.lastRecIndex,this.$refs.recCarousel.setNewRecommendation(this.recData,t);case 10:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}(),showPrevRec:function(){var e=Object(l["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:this.recData=this.recommendationList[--this.activeRecIndex];case 1:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}(),showNextRec:function(){var e=Object(l["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:this.recData=this.recommendationList[++this.activeRecIndex];case 1:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}(),getProviderList:function(){var e=Object(l["a"])(regeneratorRuntime.mark((function e(t){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return this.isLoading=!0,this.updateRecommendationStatus(t),e.next=4,T["a"].getProviderList(this.recData.name);case 4:n=e.sent,n&&n!={}&&0!==Object.keys(n).length&&(this.providerList=n.results.map((function(e){return{logo:e.logo,text:e.name,link:e.url}}))),this.$refs.recCarousel.setNewRecommendation(this.recData,t),this.isLoading=!1;case 8:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}(),updateRecommendationStatus:function(){var e=Object(l["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,T["a"].setRecommendationUserChoice(this.recData.recommendation_id,this.sessionID,this.recData.id,t);case 2:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},components:{RecommendationCarousel:R,RecommendationDescr:A}},F=I,z=(n("121a"),n("8336")),B=Object(g["a"])(F,o,c,!1,null,null,null),V=B.exports;w()(B,{VBtn:z["a"],VCard:D["a"],VCardActions:L["a"],VCardText:L["b"],VDialog:E["a"],VIcon:_["a"],VProgressCircular:S["a"]});var $={name:"Recommendation",data:function(){return{user:{},recommendation:{}}},methods:{},components:{PageHeader:i["a"],RecommendationBox:V},beforeMount:function(){var e=document.getElementsByTagName("app")[0],t=e.getAttribute("user"),n=e.getAttribute("preferences");t&&n&&(this.user=JSON.parse(t),this.preferences=JSON.parse(n))}},N=$,M=n("7496"),U=n("a75b"),H=Object(g["a"])(N,a,s,!1,null,null,null),J=H.exports;w()(H,{VApp:M["a"],VContent:U["a"]});var W=n("b8e3"),G=n("0532"),K=n("2b27"),Y=n.n(K);n("8a71"),n("49fe");r["a"].use(Y.a),new G["a"],r["a"].config.productionTip=!1,new r["a"]({vuetify:W["a"],render:function(e){return e(J)}}).$mount("#recommendation")},c4a9:function(e,t,n){},e532:function(e,t,n){"use strict";var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("a",{staticClass:"logo",attrs:{href:"/"}},[e._v("Pickee")])},a=[],s=(n("4a60"),n("2877")),i={},o=Object(s["a"])(i,r,a,!1,null,null,null);t["a"]=o.exports},ea03:function(e,t,n){},ea98:function(e,t,n){"use strict";var r=n("c4a9"),a=n.n(r);a.a}});