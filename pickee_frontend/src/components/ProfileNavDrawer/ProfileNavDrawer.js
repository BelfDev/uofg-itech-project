import Logo from "@/components/Logo/Logo.vue";
import { mdiAccountBox, mdiCog, mdiFilmstrip } from "@mdi/js"
import NavDrawerLinks from "@/components/NavDrawerLinks/NavDrawerLinks.vue"

export default {
    name: "ProfileNavDrawer",
    data: () => ({
        links: [
            {
                name: "Profile",
                url: "/profile/",
                icon: mdiAccountBox
            },

            {
                name: "Preferences",
                url: "/preferences/",
                icon: mdiCog
            },

            {
                name: "History",
                url: "/history/",
                icon: mdiFilmstrip
            },
        ]
    }),
    components: {
        Logo,
        NavDrawerLinks
    }
};
