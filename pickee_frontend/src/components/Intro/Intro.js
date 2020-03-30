import { mdiChevronRight } from "@mdi/js";

export default {
    name: "Intro",
    props: ['change-screen-method'],
    data: () => ({
        iconArrowRight: mdiChevronRight
    })
}