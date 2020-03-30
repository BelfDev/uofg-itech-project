import Vue from 'vue'
import { mdiClose, mdiAccount } from "@mdi/js";

let handleOutsideClick


// Add vue directive for the closable functionality.
// When it registers click outside of the element (except
// excluded selectors) - it runs the handler method
Vue.directive('closable', {
  bind (el, binding, vnode) {
    handleOutsideClick = (e) => {
      e.stopPropagation()
      
      const { handler, exclude } = binding.value
      let clickedOnExcludedEl = false
      
      exclude.forEach(refName => {
        if (!clickedOnExcludedEl) {
          const excludedEl = vnode.context.$refs[refName]
          clickedOnExcludedEl = excludedEl.$el.contains(e.target)
        }
      })

      if (!el.contains(e.target) && !clickedOnExcludedEl) {
        vnode.context[handler]()
      }
    }

    document.addEventListener('click', handleOutsideClick)
    document.addEventListener('touchstart', handleOutsideClick)
  },

  unbind () {
    document.removeEventListener('click', handleOutsideClick)
    document.removeEventListener('touchstart', handleOutsideClick)
  }
})

export default {
    name: "HeaderAuth",
    props: ['user'],
    methods: {
        onClose () {
            this.overlay = false
        }
    },
    data: () => ({
        overlay: false,
        iconUser: mdiAccount,
        iconClose: mdiClose
    })
}