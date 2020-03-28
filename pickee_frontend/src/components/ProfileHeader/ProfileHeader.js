import { mdiAccount } from '@mdi/js';
import api from "@/services/api";

export default {
    name: "ProfileHeader",
    props: ['user'],
    methods: {
        uploadAvatar: async function(file) {
            const response = await api.updateAvatar(this.user.id, file);
            if (response.id) {
                this.user.picture = response.picture;
            } else {
                this.errorAvatarUpload = response.picture[0] || 'Unknown upload error. Please, try different file';
            }
        }
    },
    data: () => ({
        iconUser: mdiAccount,
        avatarFile: null,
        errorAvatarUpload: ''
    })
}