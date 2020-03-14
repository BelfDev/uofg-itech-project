import Logo from "@/components/Logo/Logo.vue";
import { mdiAccountBox, mdiCog, mdiFilmstrip } from "@mdi/js"

export default {
    name: "ProfileNavDrawer",
    data: () => ({
        iconProfile: mdiAccountBox,
        iconPreferences: mdiCog,
        iconHistory: mdiFilmstrip
    }),
    components: {
        Logo
    }
};
