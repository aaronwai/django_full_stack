"use client";
import React from "react";

import { useGetUserProfileQuery } from "@/lib/redux/features/users/usersApiSlice";
import Spinner from "@/components/shared/Spinner";
import ProtectedRoute from "@/components/shared/ProtectedRoutes";

function ProfilePageContent() {
	const { data, isLoading } = useGetUserProfileQuery();
	if (isLoading) {
		return (
			<div className="flex-center pt-32">
				<Spinner size="xl" />
			</div>
		);
	}
	return (
		<div>
			<h1 className="dark:text-pumpkin text-6xl">
				{data?.profile.username}&apos;sProfile
			</h1>
		</div>
	);
}
export default function ProfilePage() {
	return (
		<ProtectedRoute>
			<ProfilePageContent />
		</ProtectedRoute>
	);
}
