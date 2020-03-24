import { mdiAccount } from '@mdi/js';

export default {
    name: "ProfileHeader",
    props: ['user'],
    data: () => ({
        iconUser: mdiAccount
    })
}