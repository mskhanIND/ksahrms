frappe.ui.form.on("Employee Service Request", {
    refresh(frm) {
        if (frm.doc.docstatus !== 1) {
            return;
        }

        const closed = ["Completed", "Rejected", "Cancelled"].includes(frm.doc.process_status);
        if (closed) {
            return;
        }

        frm.add_custom_button(__("Approve Current Step"), () => run_service_action(frm, "approve_request"));
        frm.add_custom_button(__("Reject"), () => run_service_action(frm, "reject_request"));

        if (frm.doc.process_status === "Fulfilment") {
            frm.add_custom_button(__("Mark Completed"), () => run_service_action(frm, "complete_request"));
        }
    },

    service(frm) {
        if (!frm.doc.service) {
            return;
        }

        frappe.db.get_doc("Service Catalog", frm.doc.service).then((service) => {
            frm.set_value("priority", service.default_priority || "Medium");
        });
    }
});

function run_service_action(frm, action) {
    frappe.prompt(
        [
            {
                fieldname: "comments",
                fieldtype: "Small Text",
                label: __("Comments")
            }
        ],
        (values) => {
            frappe.call({
                method: `ksa_hr_platform.api.employee_service_request.${action}`,
                args: {
                    name: frm.doc.name,
                    comments: values.comments
                },
                freeze: true,
                callback: () => frm.reload_doc()
            });
        },
        __("Update Request"),
        __("Submit")
    );
}
