"use client";
import { useGetAllUsersQuery } from "@/lib/redux/features/users/usersApiSlice";
import Spinner from "@/components/shared/Spinner";
import ProtectedRoute from "@/components/shared/ProtectedRoutes";

function TenantsPageContent() {
	const { data, isLoading } = useGetAllUsersQuery({});
	if (isLoading) {
		return (
			<div className="flex-center pt-32">
				<Spinner size="xl" />
			</div>
		);
	}
	return (
		<div>
			<h1 className="dark:text-pumpkin text-6xl">Tenants</h1>
			{data && data.profiles.results.length > 0 ? (
				data.profiles.results.map((tenant: any) => (
					<p key={tenant.id} className="dark:text-pumpkin text-4xl">
						{tenant.full_name} - {tenant.occupation}
					</p>
				))
			) : (
				<p>No tenants found</p>
			)}
		</div>
	);
}
export default function TenantsPage() {
	return (
		<ProtectedRoute>
			<TenantsPageContent />
		</ProtectedRoute>
	);
}
