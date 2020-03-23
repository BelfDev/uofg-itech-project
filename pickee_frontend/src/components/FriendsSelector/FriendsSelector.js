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

            if (friendData.data.length > 0) {
                const data = friendData.data[0];
                this.selectedFriends.push({
                    id: data.id,
                    image: data.picture,
                    text: `${data.first_name} ${data.last_name}`,
                    icon: mdiMinusCircle
                });
                this.userIDs = this.selectedFriends.map(item => item.id).join(',');
            }
        }
    },
    props: ['user'],
    data: () => ({
        selectedFriends: [],
        iconUser: mdiAccount,
        iconPlusCircle: mdiPlusCircle,
        iconPlus: mdiPlus,
        iconClose: mdiClose,
        friendEmail: null,
        dialog: false,
        userIDs: ''
    })
}