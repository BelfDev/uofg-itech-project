import { mdiClose, mdiAccount } from "@mdi/js";

export default {
    name: "HeaderAuth",
    props: ['user'],
    data: () => ({
        overlay: false,
        iconUser: mdiAccount,
        iconClose: mdiClose
    })
}