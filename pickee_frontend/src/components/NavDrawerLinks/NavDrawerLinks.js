export default {
    name: "NavDrawerLinks",
    props: ["links"],
    methods: {
        isActive(url) {
            return url === window.location.pathname;
        }
    },
    data: function() {
        return {
            test: "Test"
        }
    }
}