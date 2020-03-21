import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiPlusCircle, mdiPlus, mdiClose, mdiMinusCircle, mdiAccount } from '@mdi/js';
import http from "@/services/http";

export default {
    name: "FriendsSelector",
    components: {
        ItemList
    },
    methods: {
        removeFriend: function(targetItem) {
            const targetItemIndex = this.selectedFriends.findIndex(sourceItem => sourceItem.id === targetItem.id);
            this.selectedFriends.splice(targetItemIndex, 1);
        },
        addFriend: async function() {
            if (this.friendEmail == null) return false;

            const friendData = await http.getFriend(this.friendEmail);
            this.selectedFriends.push({
                id: friendData.id,
                image: friendData.picture,
                text: `${friendData.first_name} ${friendData.last_name} (${friendData.id})`,
                icon: mdiMinusCircle
            });
        }
    },
    props: ['user'],
    data: () => ({
        // TODO: get from API
        selectedFriends: [],
        iconUser: mdiAccount,
        iconPlusCircle: mdiPlusCircle,
        iconPlus: mdiPlus,
        iconClose: mdiClose,
        friendEmail: null,
        dialog: false
    })
}